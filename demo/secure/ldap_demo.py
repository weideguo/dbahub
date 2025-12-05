from ldap3 import Server, Connection, ALL, SUBTREE


LDAP_SERVER = "ldap.example.com"            # 替换为你的 LDAP 服务器地址
LDAP_PORT = 389                             # 389（非加密）、 636（LDAPS）
USE_SSL = False                             # LDAPS 则为 True
BIND_USER = "cn=admin,dc=example,dc=com"    # 绑定用户 DN
#BIND_USER = "uid=john,dc=example,dc=com"   # 普通用户
BIND_PASSWORD = "your_password"             # 绑定密码
SEARCH_BASE = "dc=example,dc=com"           # 搜索起点
SEARCH_FILTER = "(uid=john)"                # 搜索过滤器（ uid 为 john 的用户）
SEARCH_ATTRIBUTES = ["cn", "mail", "uid"]   # 获取这些字段的值


# 搜索所有用户
# - OpenLDAP            (objectClass=inetOrgPerson) 或 (objectClass=posixAccount)
# - Active Directory    (objectClass=user)  
# SEARCH_FILTER = "(objectClass=inetOrgPerson)"  


server = Server(LDAP_SERVER, port=LDAP_PORT, use_ssl=USE_SSL, get_info=ALL)
conn = Connection(server, user=BIND_USER, password=BIND_PASSWORD, auto_bind=True)         

# 是否连接成功，使用普通用户时，验证能否登录成功即可
#conn.bound 
# 关闭连接
#conn.unbind()

# 执行搜索
conn.search(
    search_base=SEARCH_BASE,
    search_filter=SEARCH_FILTER,
    search_scope=SUBTREE,
    attributes=SEARCH_ATTRIBUTES
)


for entry in conn.entries:
    print(entry)

