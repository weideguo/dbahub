import os
from dotenv import load_dotenv

# 从当前目录的 .env 文件中加载配置
# 也可以直接读取环境变量 export ACCESS_KEY_ID=xxx
# 以环境变量值优先
load_dotenv()

ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")


