#!/bin/env python3
import re
import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Parenthesis,Token
from sqlparse.tokens import Keyword, DML

# 返回的表名全部为小写形式，否则按照SQL中的原始形式返回
LOWER_TABLES = True

def extract_tables_by_re(statement):
    """
    使用正则提取表名
    存在问题：
    select * from a,b
    """
    table_names = set()
    table_name_pattern = r"\bFROM\s+([^\s\(\)\,]+)|\bJOIN\s+([^\s\(\)\,]+)"
    
    statement_str = statement.lower()
    matches = re.findall(table_name_pattern, statement_str, re.IGNORECASE)
    
    for match in matches:
        # 提取非空的表名部分
        for name in match:
            if name:
                # 可能存在形如 db.`tb` 
                table_names.add(name.replace("`","").lower())
                    
    return table_names
    
    
def is_subselect(parsed):
    #print(parsed,parsed.is_group)
    if not parsed.is_group:
        return False
    for item in parsed.tokens:
        #print(item.ttype,item.value)
        if item.ttype is DML and item.value.upper() in ("SELECT","UNION","UNION ALL"):
            return True
    return False


def extract_from_part(parsed):
    """
    从特定的谓词 "FROM", "JOIN", "LEFT JOIN", "RIGHT JOIN" 后获取token，以及子查询
    """
    def get_part_from_group(item):
        if isinstance(item,Parenthesis):
            yield from extract_from_part(item)
        elif item.is_group:
            for nitem in item.tokens:
                yield from get_part_from_group(nitem)
    
    from_seen = False
    before_item = None
    for item in parsed.tokens:
        #print(item,item.is_group,from_seen,"--------")
        if is_subselect(item):
            # 子查询
            yield from extract_from_part(item)
        elif from_seen:
            #print(item,item.value,is_subselect(item),isinstance(item,Identifier),item.is_group,"---------------xx")
            if item.value.upper() in ("UNION","UNION ALL"):
                from_seen = False
                continue
            
            if item.is_group and not (isinstance(item,Identifier) or isinstance(item,IdentifierList)):
                # 如where x in (select x ...) 这种形式的子查询
                yield from get_part_from_group(item)
            elif item.ttype is Keyword and item.value.upper() in ("ORDER BY","GROUP BY"):
                # 没有这个判断会导致 order by、GROUP BY 之后的被错误当成表
                #print(item.value,item,item.ttype,item.is_group,type(item),"----------xxx")
                return
            else:                        
                yield item
                  
                
        elif item.ttype is Keyword and item.value.upper() in ("FROM", "JOIN", "LEFT JOIN", "RIGHT JOIN"):
            from_seen = True
        
        before_item = item


def get_tablename(item):  
    #return item.get_real_name().replace("`","").lower()       # 这个获取不到库名
    t = str(item).split(" ")[0].replace("`","")
    return t.lower() if LOWER_TABLES else t


def extract_table_identifiers(token_stream):
    """
    从 "FROM", "JOIN", "LEFT JOIN", "RIGHT JOIN" 后一token获取表名
    """
    def get_tablename_from_item(item):
        
        if len(item.tokens) >1 and isinstance(item.tokens[0],Parenthesis):
            # 为子查询时 (select * from aa) xx
            for ssitem in item.tokens:
                if ssitem.ttype is None:
                    #print(ssitem.value,ssitem.tokens)
                    table_item = extract_from_part(ssitem)
                    yield from extract_table_identifiers(table_item)
            pass
        else:
            # 不是子查询时
            yield get_tablename(item)    
       
    for item in token_stream:
        #print(item)
        if isinstance(item, IdentifierList):
            # from a,b 这种情况时
            for sub_item in item.get_identifiers():
                #print(sub_item,sub_item.is_group,type(sub_item))
                if not isinstance(sub_item, Identifier):
                    continue
                
                yield from get_tablename_from_item(sub_item)
                
        elif isinstance(item, Identifier):
            #print(item,type(item),"xxxx")
            yield from get_tablename_from_item(item)
        

def extract_tables(sql):
    parsed = sqlparse.parse(sql)[0]
    table_names = set()
    # 有些语句难以判断为子查询，使用正则直接提取
    #table_names = extract_tables_by_re(parsed.value )
    #print(table_names)
    stream = extract_from_part(parsed)
    for t in extract_table_identifiers(stream):
        table_names.add(t)
    return table_names


if __name__ == "__main__":
    
    #import sqlparse
    #sql = "SELECT * FROM    (  SELECT id FROM users  )     aaaa"
    #parsed = sqlparse.parse(sql)[0]
    #item = parsed.tokens[-1]
    
    sql_queries = [   
        ({"users"},                     "SELECT * FROM USERS",                                                                                                                                    ),
        ({"users"},                     "SELECT a,b,c FROM USERS",                                                                                                                                ),
        ({"users"},                     "SELECT cc.a as aa,b,c FROM USERS cc",                                                                                                                    ),
        ({"users"},                     "SELECT * FROM USERS cc",                                                                                                                                 ),
        ({"users"},                     "SELECT * FROM USERS as cc",                                                                                                                              ),
        ({"ab.users",},                 "SELECT * FROM ab.USERS",                                                                                                                                 ),        
        ({"users",},                    "SELECT * FROM users where a=1",                                                                                                                          ),
        ({"users",},                    "SELECT id,count(*) FROM users where a=1 group by id",                                                                                                    ),
        ({"users","orders",},           "select * from orders o,(SELECT id,count(*) c FROM users where a=1 group by id) a1 where o.id=u.id",                                                      ),
        ({"users","orders",},           "select idx,(SELECT id,count(*) c FROM users where a=1 group by id) from orders",                                                                         ),
        ({"users",},                    "SELECT * FROM users cc where a=1 order by id asc limit 100,10",                                                                                          ), 
        ({"users",},                    "SELECT * FROM users cc where a=1 order by id limit 100,10",                                                                                              ), 
        ({"orders","ab.users",},        "SELECT u.name FROM ab.`users` u JOIN orders o ON u.id = o.user_id",                                                                                      ),
        ({"orders","users"},            "SELECT u.name FROM users u right JOIN orders o ON u.id = o.user_id",                                                                                     ),
        ({"orders","users"},            "SELECT u.name FROM users u, orders o ON u.id = o.user_id",                                                                                               ),
        ({"bbb","users"},               "SELECT * FROM (SELECT id FROM users a,bbb b where a.id=b.id ) aaaa",                                                                                     ),
        ({"aaa","users"},               "SELECT * FROM users a ,(select a from aaa) x on a.id=x.id",                                                                                              ),
        ({"aaa","xxx111",},             "SELECT * FROM (select a from xxx111) a , (select a from aaa) x on a.id=x.id",                                                                            ),
        ({"aaa","xxx111",},             "SELECT * FROM (select a from xxx111) a join (select a from aaa) x on a.id=x.id",                                                                         ), 
        ({"aaa","xxx111",},             "SELECT * FROM (select a from xxx111) a left join (select a from aaa) x on a.id=x.id order by 1,2 desc limit 10",                                         ), 
        ({"aaa","users",},              "SELECT a,b,(select count(*) from aaa) FROM users",                                                                                                       ),
        ({"aaa","users",},              "SELECT a,b,(select count(*) from aaa a where a.user=u.user) FROM users u",                                                                               ),
        ({"aaa","bbb","users",},        "SELECT a,b,(select count(*) from aaa a,bbb b on a.user=b.user) FROM users u",                                                                            ),
        ({"aaa","bbb","users",},        "SELECT a,b,(select count(*) from aaa a,bbb b where a.user=b.user) FROM users u",                                                                         ),
        ({"aaa","bbb",},                "SELECT a.b FROM aaa WHERE (a = 0 AND EXISTS (SELECT 1 FROM bbb WHERE id = aaa.a_id ))",                                                                  ),
        ({"aaa","users",},              "SELECT * FROM users where a in (select a from aaa)",                                                                                                     ),
        ({"aaa","bbb","users",},        "SELECT * FROM users where a in (select a from aaa where b in (select b from bbb))",                                                                      ),
        ({"aaa","bbb","users",},        "SELECT * FROM users where a in (select a from aaa a join bbb b on a.id=b.id)",                                                                           ),
        ({"aaa","bbb","users",},        "SELECT * FROM users where a in (select a from aaa a,bbb b where a.id=b.id)",                                                                             ),
        ({"aaa","users",},              "SELECT a,b FROM users union select a,b from aaa",                                                                                                        ),
        ({"aaa","users",},              "SELECT a,b FROM users union all select a,b from aaa",                                                                                                        ),
        ({"f","i","g","h","b","c","d","j","k","e","a",},"select K.a,K.b from (select H.b from (select G.c from (select F.d from (select E.e from A, B, C, D, E) cc , F) dd  , G), H), I, J, K order by 1,2;",     ),
        
    ]                                                                               
    
    
    for _tables,sql in sql_queries:
        tables = extract_tables(sql)
        if tables != _tables:
            print(f"SQL:{sql}")
            print(f"Tables:{tables}")
    
        
    
    sql="""
    """
    
    LOWER_TABLES = False
    #tables = ','.join(extract_tables(sql))
    #print('Tables: {}'.format(tables))
    