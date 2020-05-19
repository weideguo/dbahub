#!/bin/env python
#coding:utf8
#
#用于文件模式匹配
#比如文件安全检查

import os
import yara


"""
下载yara规则
https://github.com/Yara-Rules/rules
其他yara规则收录
https://github.com/InQuest/awesome-yara     
文档
https://yara.readthedocs.io/
"""
#存在yara规则的路径
rule="/path2rule"
filepath = {}
index=0
for dirpath, dirs, files in os.walk(rule):
    for file in files:
        ypath = os.path.join(dirpath, file)
        key = "rule" + str(index)
        filepath[key] = ypath
        index += 1
        
yararule = yara.compile(filepaths=filepath)

#要检测的文件
filename="/tmp/test.sh"
fp=open(filename,"rb")
matches = yararule.match(data=fp.read())

print(matches[0].rule)
print(matches[0].tags)
print(matches[0].strings)



rule = yara.compile(source='rule foo: bar {strings: $a = "lmn" condition: $a}')
matches = rule.match(data='abcdefgjiklmnoprstuvwxyz')

s="""
rule url {
    meta:
        author = "Antonio S. <asanchez@plutec.net>"
    strings:
        $url_regex = /https?:\/\/([\w\.-]+)([\/\w \.-]*)/ wide ascii
    condition:
        $url_regex
}
"""
rule = yara.compile(source=s)
matches = rule.match(data="https://sss.com/a")

