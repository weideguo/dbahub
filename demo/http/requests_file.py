#coding:utf8
# requests 上传文件

'''
from flask import Flask,
app = Flask(__name__)
@app.route('/upload/',methods=['GET','PUT','POST'])
def test4():
    """
    curl "http://this_host/upload/" -F "filename=@/root/x.txt"  
    Content-Type: multipart/form-data; 
    """
    print(request.headers)
    file = request.files.get('filename')
    file.save('/tmp/aaa.txt')
    return "uploal success"

'''

import requests
#fr=request.FILES.get('file',None) 
filename='/tmp/tmpKrm6PK'
fr=open(filename,'rb')
#fr=open(filename,'r')
file = {'filename': fr}
url='http://127.0.0.1:4000/upload/'
r = requests.post(url, files=file)

print(r.text)




import os
import requests
from urllib3 import encode_multipart_formdata

def post_file(url, filename):
    """
    上传文件
    使用更底层的消息构造
    """
    file_name = filename.split("/")[-1]
    with open(filename, "rb") as f:
        length = os.path.getsize(filename)
        data = f.read()
    
    file_data = {
        "filename": file_name,
        "filelength": length,
    }
    file_data["file"] = (file_name, data)
    encode_data = encode_multipart_formdata(file_data)
    _file_data = encode_data[0]
    
    headers = {"Content-Type": "application/octet-stream"}
    headers['Content-Type'] = encode_data[1]
    
    return requests.post(url, data=_file_data, headers=headers)

