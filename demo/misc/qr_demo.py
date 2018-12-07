import pyqrcode

"""
pyqrcode
pypng
"""

a="http://httpbin.org"
a=u"中文"
qr=pyqrcode.create(a)
file_path="./test.png"
qr.png(file_path,scale=5)      			#导出png
print(qr.terminal()) 	              #终端打印
