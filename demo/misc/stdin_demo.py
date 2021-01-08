#encoding:utf8


import sys

"""
echo "some string" | python stdin_demo.py
python stdin_demo.py <<< "some string"
python stdin_demo.py < file_name

python stdin_demo.py <<eof
some string1111
some string222
eof

"""

r=sys.stdin       #<open file '<stdin>', mode 'r' ...>
x=r.readline()
while x:
    print(x.strip())
    x=r.readline()

"""
for k in r:
    print(k.strip())
"""


print("xxxx")
sys.stdout.flush()


while True:
    line = sys.stdin.readline()
    if not line:
        break
    sys.stdout.write(line)
    sys.stdout.flush()
    
    

