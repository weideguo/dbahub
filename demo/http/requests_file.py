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


