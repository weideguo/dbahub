# -*-coding: utf-8 -*-

"""
protobuf实现序列化与反序列化
###########################################################
pip install protobuf            
yum install protobuf-compiler   
protoc -I=./ --python_out=./ helloworld.proto   #编译proto成py
############################################################
#pip install grpcio   #使用grpc才需要
pip install grpcio-tools
pip install protobuf 
python -m grpc_tools.protoc --python_out=. -I. helloworld.proto     #编译proto成py
"""


from helloworld_pb2 import helloworld

filename="mybuffer.bak"

def serialize():
    hw = helloworld()
    hw.id = 123
    hw.str = "eric"
    #hw.wow = 1       #proto文件中指定为optional，则为非必需
    print(hw)

    with open(filename, "wb") as f:
        f.write(hw.SerializeToString())



def reserialize():
    hw = helloworld()
    with open(filename, "rb") as f:
        hw.ParseFromString(f.read())
        print(hw)


if __name__ == "__main__":
    serialize() 
    print("-------------------------------reserialize done-------------------------------")
    reserialize()
    print("-------------------------------reserialize done-------------------------------")
       
    


