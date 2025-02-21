from minio import Minio


endpoint = "10.30.20.160:9000"                              #
access_key = "jjjjjjjjjjjjjjjjjjjj"                         # 需要先在minio中创建access_key
secret_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"     #
bucket_name = "my-bucket-20250217"                          #
file_path = "/tmp/test.txt"                                 #
object_name = "test.txt"                                    #在minio中的相对路径



minio_client = Minio(
    endpoint,
    access_key=access_key,
    secret_key=secret_key,
    secure=False                        # http与否
)


#found = minio_client.bucket_exists(bucket_name)    # 判断bucket是否存在
#minio_client.make_bucket(bucket_name)              # 创建bucket

# 上传文件
put_response = minio_client.fput_object(bucket_name, object_name, file_path) 

# 下载文件
get_response = minio_client.get_object(bucket_name, object_name)

# 保存成文件 
with open("/tmp/test2.txt", "wb") as f:
    f.write(get_response.data) 

