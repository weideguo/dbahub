
# re模块扩展的正则表达式语法 
# (?P=<name>) 定义取的字符串的正则表达式
# (?P=name)   引用定义取的字符串

import re
rgx = re.compile('{{(?P<_name_>[^{}]+)}}')
templ_str = "echo  {{before.stdout_map_desc}}  {{session.aa}}  {{global.aa}}  {{select.aa}} "

variable_names = {match.group('_name_') for match in rgx.finditer(templ_str)}
print(variable_names)  



import re
sentence = 'cats are fast'  
regex = re.compile('(?P<animal1>\w+) (?P<verb1>\w+) (?P<adjective1>\w+)')  
matched = re.search(regex, sentence)  
print(matched.groupdict())  


