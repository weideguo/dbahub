"""
pip install PyJWT 
# JSON Web Token
"""
import jwt

payload = {"some": "payload"}
key = "my_secret_test"

# 生成jwt格式的token
jwt_encoded = jwt.encode(payload, key)

# 由jwt获取payload
jwt.decode(jwt_encoded, key)


"""
安全要求不高的场景，仅需要校验jwt的合法性，校验payload的时间字段等，无需查询数据库对payload进行值校验。
其他场景可以选择查询数据库或缓存对payload进行校验
"""
