# -*- coding: UTF-8 -*-
from pymongo import message
from pymongo.message import *

p_coll           = None               
p_spec           = None        
p_projection     = None        
p_skip           = None        
p_limit          = None        
p_batch_size     = None    
p_options        = None    
p_read_concern   = None    
p_collation      = None    
p_session        = None    
p_allow_disk_use = None


def _gen_find_command(
    coll,
    spec,
    projection,
    skip,
    limit,
    batch_size,
    options,
    read_concern,
    collation=None,
    session=None,
    allow_disk_use=None,
):
    coll           =  p_coll            if p_coll            else coll          
    spec           =  p_spec            if p_spec            else spec          
    projection     =  p_projection      if p_projection      else projection    
    skip           =  p_skip            if p_skip            else skip          
    limit          =  p_limit           if p_limit           else limit         
    batch_size     =  p_batch_size      if p_batch_size      else batch_size    
    options        =  p_options         if p_options         else options       
    read_concern   =  p_read_concern    if p_read_concern    else read_concern  
    collation      =  p_collation       if p_collation       else collation     
    session        =  p_session         if p_session         else session       
    allow_disk_use =  p_allow_disk_use  if p_allow_disk_use  else allow_disk_use
    
    """以下为pymongo.message._gen_find_command原始定义，直接从原文件复制过来即可，不要引用函数名，否则会导致循环递归"""
    cmd = SON([("find", coll)])
    if "$query" in spec:
        cmd.update(
            [
                (_MODIFIERS[key], val) if key in _MODIFIERS else (key, val)
                for key, val in spec.items()
            ]
        )
        if "$explain" in cmd:
            cmd.pop("$explain")
        if "$readPreference" in cmd:
            cmd.pop("$readPreference")
    else:
        cmd["filter"] = spec
    
    if projection:
        cmd["projection"] = projection
    if skip:
        cmd["skip"] = skip
    if limit:
        cmd["limit"] = abs(limit)
        if limit < 0:
            cmd["singleBatch"] = True
    if batch_size:
        cmd["batchSize"] = batch_size
    if read_concern.level and not (session and session.in_transaction):
        cmd["readConcern"] = read_concern.document
    if collation:
        cmd["collation"] = collation
    if allow_disk_use is not None:
        cmd["allowDiskUse"] = allow_disk_use
    if options:
        cmd.update([(opt, True) for opt, val in _OPTIONS.items() if options & val])
    
    print(cmd)
    return cmd



def apply_patch():
    message._gen_find_command = _gen_find_command


"""
# 使用

import mongo_patch

mongo_patch.p_coll           = "collection_test"
mongo_patch.p_spec           = {"name":9}         
mongo_patch.p_projection     = {"title":1}                      
mongo_patch.p_limit          = 3  

mongo_patch.apply_patch()

# db.collection_test.find({"name":9}, {"title":1}).limit(3)

"""

