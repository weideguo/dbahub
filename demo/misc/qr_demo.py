import pyqrcode

"""
pyqrcode
pypng
"""

string="http://httpbin.org"
qr=pyqrcode.create(string)
file_path="./test.png"
qr.png(file_path,scale=5)      			#导出png
print(qr.terminal()) 	  #终端打印
