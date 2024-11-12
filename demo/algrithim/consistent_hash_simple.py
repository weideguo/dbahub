"""
一个非常简单的一致性hash样例
实现当节点变化是，受影响的key能迁移到其他节点
但不实现节点变化后的均匀分布
"""

def dispatch_keys(all_keys):
    """
    若干个key按照 mod 8，构成hash环分配到四个节点上
    """
    server_0 = []
    server_1 = []
    server_2 = []
    server_3 = []

    
    for k in all_keys:
        m = k % 8
        if m >=0 and m <=1:
            server_0.append(k)
        if m >1 and m <=3:
            server_1.append(k)
        if m >3 and m <=5:
            server_2.append(k)
        if m >5 and m <=7:
            server_3.append(k)
    
    # 输出每个节点拥有的key的信息
    print("server_0 [0,1]:",server_0)
    print("server_1 (1,3]:",server_1)
    print("server_2 (3,5]:",server_2)
    print("server_3 (5,7]:",server_3)

def dispatch_keys_del(all_keys):
    """
    若干个key按照 mod 8，构成hash环分配到四个节点上，在此基础上去掉一个节点
    """
    server_0 = []
    server_1 = []
    #server_2 = []
    server_3 = []
    
    
    for k in all_keys:
        m = k % 8
        if m >=0 and m<=1:
            server_0.append(k)
        if m >1 and m<=3:
            server_1.append(k)
        if m >3 and m<=5:
            #server_2.append(k)
            server_3.append(k)
        if m >5 and m<=7:
            server_3.append(k)
    
    # 输出每个节点拥有的key的信息
    print("server_0 [0,1]:",server_0)
    print("server_1 (1,3]:",server_1)
    #print("server_2 (3,5]:",server_2)
    print("server_3 (5,7]:",server_3)

def dispatch_keys_add(all_keys):
    """
    若干个key按照 mod 8，构成hash环分配到四个节点上，在此基础上增加一个节点
    """
    server_0 = []
    server_1 = []
    server_2 = []
    server_3_0 = []
    server_3 = []
    
    
    for k in all_keys:
        m = k % 8
        if m >=0 and m<=1:
            server_0.append(k)
        if m >1 and m<=3:
            server_1.append(k)
        if m >3 and m<=5:
            server_2.append(k)
        if m >5 and m<=6:
            server_3_0.append(k)
        if m >6 and m<=7:
            server_3.append(k)
    
    # 输出每个节点拥有的key的信息
    print("server_0   [0,1]:",server_0)
    print("server_1   (1,3]:",server_1)
    print("server_2   (3,5]:",server_2)
    print("server_3_0 (3,6]:",server_3_0)
    print("server_3   (6,7]:",server_3)

if __name__ == "__main__":
    all_keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    print("---------------------------")
    dispatch_keys(all_keys)
    print("---------------------------delete 1 node")
    dispatch_keys_del(all_keys)
    print("---------------------------add 1 node")
    dispatch_keys_add(all_keys)
