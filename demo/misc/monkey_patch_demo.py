#coding:utf8

#通过引入模块实现已有功能替换，但不破坏已有功能的代码

import json
import ujson
 
 
def monkey_patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads
 
 
monkey_patch_json()    

"""
import json
import monkey_patch_demo     #引入该模块即可实现对json模块功能的替换

"""
