import re

def is_ip(ip):
    r=re.search('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$',ip)
    if r:
        return True
    else:
        return False
        
        
