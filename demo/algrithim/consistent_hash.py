
import md5
class HashRing(object):
    def __init__(self, nodes=None, replicas=3):
        """Manages a hash ring.
        `nodes` is a list of objects that have a proper __str__ representation.
        `replicas` indicates how many virtual points should be used pr. node,
        replicas are required to improve the distribution.
        """
        self.replicas = replicas
        self.ring = dict()
        self._sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)
    def add_node(self, node):
        """Adds a `node` to the hash ring (including a number of replicas).
        """
        for i in xrange(0, self.replicas):
            key = self.gen_key('%s:%s' % (node, i))
            print("node %s-%s key is %ld" % (node, i, key))
            self.ring[key] = node
            self._sorted_keys.append(key)
        self._sorted_keys.sort()
    def remove_node(self, node):
        """Removes `node` from the hash ring and its replicas.
        """
        for i in xrange(0, self.replicas):
            key = self.gen_key('%s:%s' % (node, i))
            del self.ring[key]
            self._sorted_keys.remove(key)
    def get_node(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned.
        If the hash ring is empty, `None` is returned.
        """
        return self.get_node_pos(string_key)[0]
    def get_node_pos(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned
        along with it's position in the ring.
        If the hash ring is empty, (`None`, `None`) is returned.
        """
        if not self.ring:
            return None, None
        key = self.gen_key(string_key)
        nodes = self._sorted_keys
        for i in xrange(0, len(nodes)):
            node = nodes[i]
            if key <= node:
                print("string_key %s key %ld" % (string_key, key)) 
                print("get node %s-%d " % (self.ring[node], i))
                return self.ring[node], i
        return self.ring[nodes[0]], 0
    def print_ring(self):
        if not self.ring:
            return None, None
        nodes = self._sorted_keys
        for i in xrange(0, len(nodes)):
            node = nodes[i]
            print("ring slot %d is node %s, hash vale is %s" % (i, self.ring[node], node))
    def get_nodes(self, string_key):
        """Given a string key it returns the nodes as a generator that can hold the key.
        The generator is never ending and iterates through the ring
        starting at the correct position.
        """
        if not self.ring:
            yield None, None
        node, pos = self.get_node_pos(string_key)
        for key in self._sorted_keys[pos:]:
            yield self.ring[key]
        while True:
            for key in self._sorted_keys:
                yield self.ring[key]
    def gen_key(self, key):
        """Given a string key it returns a long value,
        this long value represents a place on the hash ring.
        md5 is currently used because it mixes well.
        """
        m = md5.new()
        m.update(key)
        return long(m.hexdigest(), 16)
        """
        hash = 0
        for i in xrange(0, len(key)):
            hash += ord(key[i]) 
        return hash
        """
 
if __name__ == "__main__":
    nodes = ['a','g','z']
    
    ring = HashRing(nodes,1)
    
    ring.print_ring()
    ring.add_node('0000')
    ring.add_node('1111')
    ring.add_node('2222')
    ring.add_node('3333')
    ring.add_node('4444')
    
    ring.get_node('0000')
    ring.get_node('1111')
    ring.get_node('2222')
    ring.get_node('3333')
    ring.get_node('4444')
    

