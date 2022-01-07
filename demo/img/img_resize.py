#!/bin/env python3
# -*- coding: utf-8 -*-
# 批量更改图片的尺寸

import os
from PIL import Image
from traceback import format_exc

path = "/root/img_test/kf"
to_size=100


if path[-1]=="/":
    path=path[:-1]
        
_path=path+"_new"
if not os.path.isdir(_path):
    os.makedirs(_path)
        
fs=os.listdir(path)

for f in fs:
    try:
        _file=os.path.join(path,f)
        im=Image.open(_file)
        x,y=im.size
    
        if x>y:
            _x=to_size
            _y=y*_x/x
        else:
            _y=to_size
            _x=x*_y/y
    
        _x=int(_x)
        _y=int(_y)
    
        out=im.resize((_x,_y),Image.ANTIALIAS) 
        try: 
            out.save(os.path.join(_path,f))
        except:
            # 有些图片可能以png结尾，但确以jpg为后缀，因此需要额外处理
            os.remove(os.path.join(_path,f))
            out=out.convert("RGB")
            out.save(os.path.join(_path,f),quality=95)
            #out.save(os.path.join(_path,f.split(".")[0]+".png"))
    except:
        print(format_exc())
        print(f)
 
