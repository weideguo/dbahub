"""
在简单的一致性hash上引入虚拟节点，实现key在真实节点变化时分布更加均匀
通过增加虚拟节点个数，增加分布的均匀性
"""

def dispatch_keys(all_keys):
    """
    若干个key按照 mod 8，构成hash环分配到8个虚拟节点上，再把虚拟节点分配到真实节点
    """
    v_server_0 = []
    v_server_1 = []
    v_server_2 = []
    v_server_3 = []
    v_server_4 = []
    v_server_5 = []
    v_server_6 = []
    v_server_7 = []

    
    for k in all_keys:
        m = k % 8
        if m >=0 and m <1:
            v_server_0.append(k)
        if m >=1 and m <2:
            v_server_1.append(k)
        if m >=2 and m <3:
            v_server_2.append(k)
        if m >=3 and m <4:
            v_server_3.append(k)
        if m >=4 and m <5:
            v_server_4.append(k)
        if m >=5 and m <6:
            v_server_5.append(k)
        if m >=6 and m <7:
            v_server_6.append(k)
        if m >=7 and m <8:
            v_server_7.append(k)

            
    # 输出每个节点拥有的key的信息
    # 虚拟节点到真实节点的映射应避开相邻虚拟节点对应相邻真实节点，以免虚拟节点上key的迁移最终都映射到下一个真实节点
    # 如将虚拟节点名md5后再取 mod ?
    print("server_0 [v_server_0,v_server_3]:",v_server_0,v_server_3)
    print("server_1 [v_server_1,v_server_6]:",v_server_1,v_server_6)
    print("server_2 [v_server_2,v_server_5]:",v_server_2,v_server_5)
    print("server_3 [v_server_4,v_server_7]:",v_server_4,v_server_7)


def dispatch_keys_del(all_keys):
    """
    删除一个节点
    """
    v_server_0 = []
    v_server_1 = []
    v_server_2 = []
    v_server_3 = []
    v_server_4 = []
    v_server_5 = []
    v_server_6 = []
    v_server_7 = []

    
    for k in all_keys:
        m = k % 8
        if m >=0 and m <1:
            v_server_0.append(k)
        if m >=1 and m <2:
            v_server_1.append(k)
        if m >=2 and m <3:
            #v_server_2.append(k)
            v_server_3.append(k)
        if m >=3 and m <4:
            v_server_3.append(k)
        if m >=4 and m <5:
            v_server_4.append(k)
        if m >=5 and m <6:
            #v_server_5.append(k)
            v_server_6.append(k)
        if m >=6 and m <7:
            v_server_6.append(k)
        if m >=7 and m <8:
            v_server_7.append(k)

            
    # 输出每个节点拥有的key的信息
    print("server_0 [v_server_0,v_server_3]:",v_server_0,v_server_3)
    print("server_1 [v_server_1,v_server_6]:",v_server_1,v_server_6)
    #print("server_2 [v_server_2,v_server_5]:",v_server_2,v_server_5)   # 删除的节点为这个
    print("server_3 [v_server_4,v_server_7]:",v_server_4,v_server_7)    
    
    
if __name__ == "__main__":
    all_keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    print("---------------------------")
    dispatch_keys(all_keys)    
    print("---------------------------delete 1 node")
    dispatch_keys_del(all_keys) 
    