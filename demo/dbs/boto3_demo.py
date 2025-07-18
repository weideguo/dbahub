"""
s3协议
pip install boto3

# 默认使用的配置
~/.aws/credentials
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET

~/.aws/config
[default]
region=us-east-1
"""
import os
import boto3

ENDPOINT_URL = "http://xxxx"                       # 自定义的服务，
ACCESS_KEY_ID = ""
SECRET_ACCESS_KEY = ""
REGION_NAME = ""

BUCKET_NAME = ""

s3 = boto3.client(
    "s3",                                           # 使用s3服务
    endpoint_url = ENDPOINT_URL,
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)


# 要上传的文件名
file_path = ""
# 存放于s3的名字
s3_key = os.path.basename(file_path)


# 上传文件
s3.upload_file(
    file_path,
    BUCKET_NAME,
    s3_key
)

# 生成临时上传信息
expires_in = 3600
presigned_post = s3.generate_presigned_post(
    Bucket=BUCKET_NAME,
    Key=s3_key,
    Fields=None,            # 可添加额外表单字段
    Conditions=None,        # 可添加条件限制
    ExpiresIn=expires_in
)

"""
返回为字典格式
curl -X POST "$presigned_post.url"  \        # 字典中的url
 -F $presigned_post.fields.k1=v1    \
 -F $presigned_post.fields.k2=v2    \
 ....                               \        # 包含所有字典返回的key value              
 -F "file=@/root/test20250715_111.txt"       # 本地文件路径
 
"""


# 下载到本地的文件名
local_path = ""
        
# 下载文件
s3.download_file(BUCKET_NAME, s3_key, local_path)


# 直接读取内容
response = s3.get_object(Bucket=BUCKET_NAME, Key=s3_key)
response_data = response["Body"].read()


# 生成临时下载url
expires_in = 3600        # 过期时间，秒
download_url = s3.generate_presigned_url(
    ClientMethod="get_object",
    Params={
        "Bucket": BUCKET_NAME,
        "Key": s3_key
    },
    ExpiresIn=expires_in
)
"""
后端可直接返回给前端，从而实现下载不需要经过后端中转
直接用GET 方法请求url即可实现下载
"""

