# -*- coding: UTF-8 -*-
import geolite2
import maxminddb
"""
pip install maxminddb-geolite2==2018.703
"""

def get_location(ip):
    default_str = 'Unknown' 
    
    if ip is None:
        return default_str
    
    with maxminddb.open_database(geolite2.geolite2_database()) as reader:
        try:
            match = reader.get(ip)
        except:
            return default_str
        # 语言优先级
        lang_priority = ['zh-CN','en']
        # 获取的字段顺序
        fields = ['country','city']
        locations = []
        for field in fields:
            field_value = default_str
            for lang in lang_priority:
                if field_value != default_str:
                    break
                try:
                    field_value = match[field]['names'][lang]
                except:
                    pass
            
            locations.append(field_value)
        return ' '.join(locations)
 

ip = '1.1.1.1'
 
print(get_location(ip))

          
reader = maxminddb.open_database(geolite2.geolite2_database())
match = reader.get(ip)
print(match)


