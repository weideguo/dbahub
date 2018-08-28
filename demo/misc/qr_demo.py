import pyqrcode

"""
pyqrcode
pypng
"""

string="http://httpbin.org"
qr=pyqrcode.create(string)
qr.png(file)      			#导出png
print(qr.terminal()) 	  #终端打印
