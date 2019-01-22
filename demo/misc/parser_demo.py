#coding:utf8

import optparse



usage = "Usage: %prog [options] [FILE]"
usage += "\n\nother line to say something."


parser = optparse.OptionParser(usage=usage)
parser.add_option('-H', '--host', help='connect to HOST (default localhost)')
parser.add_option('-p', '--port', help='connect to PORT (default 6379)')
parser.add_option('-s', '--socket', help='connect to SOCKET')
parser.add_option('-w', '--password', help='connect with PASSWORD')

parser.print_help()

options, args = parser.parse_args()

print options

"""
{'host': '127.0.0.1', 'password': None, 'port': None, 'socket': None}
"""

print args

"""
['sds', 'dk']
"""

"""
python parser_demo.py -H 127.0.0.1 sds dk
"""
