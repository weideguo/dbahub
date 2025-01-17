# python3
# 一种通过 public_key private_key 提供api的方法

import hashlib

def get_sign(public_key, private_key, params, timestamp):
    """
    params 为字典类型
    """
    params["timestamp"] = timestamp
    params["publicKey"] = public_key
    params_str = "&".join(["%s=%s" % (k, params[k]) for k in sorted(params.keys())])
    # private_key 参与加密但不加入传输参数
    total_str = "%s&privateKey=%s" % (params_str, private_key)   # 约定好格式，确保客户端、服务端格式一致即可
    md5 = hashlib.md5()
    md5.update(total_str.encode("utf-8"))
    params["sign"] = md5.hexdigest()
    return params["sign"]
    

if __name__=="__main__":
    params = {"a":"中文","c":"adsafd","b":"123"}
    sign = get_sign("my_test_public_key", "f967a2f1777463aabcede12324888888", params, 1700000000)
    # 实际使用参数
    print(params)
    
    """
    请求参数：
    a=xxx&b=xxx&c=xxx&publicKey=xxx&timestamp=xxx&sign=xxxxx
    
    服务端校验：
    timestamp 
    sign      
    
    重放攻击防护方法：
    短期记录sign？如果存在则不允许
    严格要求timestamp？如果当前时间超过n秒则不允许
    """
    
