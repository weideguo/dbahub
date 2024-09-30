# pip install dnslib

import dns.resolver

#a=dns.resolver.query("www.a.com", "CNAME")
a=dns.resolver.resolve("www.a.com", "CNAME")
a.rrset

