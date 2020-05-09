#coding:utf8

import sys
import optparse



usage = "Usage: %prog [options] [FILE]"
usage += u"\n\n中文other line to say something."


parser = optparse.OptionParser(usage=usage)
parser.add_option('-H', '--host', help='connect to HOST (default localhost)')
parser.add_option('-p', '--port', help='connect to PORT (default 6379)')
parser.add_option('-s', '--socket', type="int", help='connect to SOCKET')
parser.add_option('-w', '--password',default="xxxx", help=u'中文connect with PASSWORD')

parser.add_option('-v', '--verbose', help='verbose xxxx')
parser.add_option("--noisy",action="store_const", const=2, dest="verbose")

if len(sys.argv)<=1:
    parser.print_help()
else:
    options, args = parser.parse_args()

    print(options)
    print(args)
    

"""
{'host': '127.0.0.1', 'password': None, 'port': None, 'socket': None}

['sds', 'dk']

python parser_demo.py -H 127.0.0.1 sds dk
"""
