import struct
import math


def bmp_header(data):
    return b"BM" \
        + struct.pack("<l", 14 + 40 + 8 + len(data)) \
        + b"\x00\x00" \
        + b"\x00\x00" \
        + b"\x3e\x00\x00\x00" \
        + b"\x28\x00\x00\x00" \
        + struct.pack("<l", len(data)) \
        + b"\x01\x00\x00\x00" \
        + b"\x01\x00" \
        + b"\x01\x00" \
        + b"\x00\x00\x00\x00" \
        + struct.pack("<l", math.ceil(len(data) / 8)) \
        + b"\x00\x00\x00\x00" \
        + b"\x00\x00\x00\x00" \
        + b"\x00\x00\x00\x00" \
        + b"\x00\x00\x00\x00" \
        + b"\x00\x00\x00\x00\xff\xff\xff\x00"
        
       
data=b"who am i"   
#将数据伪造成bmp文件    
bmp_data=bmp_header(data)+data

filename="xx.bmp"
with open(filename,"wb") as f:
    f.write(bmp_data)



