#coding:utf8

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String ,DateTime, Boolean

# 连接数据库
engine = create_engine('mysql://root:password@127.0.0.1:3306/db_name?charset=utf8')

Base = declarative_base()

class News(Base): 
    __tablename__ = 'students1'
    id = Column(Integer, primary_key = True)
    nickname = Column(String(20))
    name = Column(String(20), nullable = False)
    in_time = Column(DateTime)
    is_vaild = Column(Boolean)
    idcard = Column(Integer, unique = True)
 

# 创建表格 
News.metadata.create_all(engine)   


if __name__ == "__main__":
    
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)

    ## insert

    new1 = News(
        nickname = 'aaa',
        name = 'bbb',
    )
    session.add(new1)
    #session.add_all([new1,new2]) #插入多条
    session.commit()



    ## select       
    return session.query(News).get(10)   #使用主键？ 
    return session.query(News).filter_by(is_vaild=True)


    ## update
    data_list = session.query(News).filter(News.id >= 5)
    for item in data_list:
        if item:
            item.is_vaild = 0 
            session.add(item)  
    session.commit() 
    
    
    ## delete
    data = session.query(News).get(8)
    session.delete(data)
    session.commit()

    
    delete_list = session.query(News).filter(News.id <= 5)
    for item in delete_list:
        if item:
            session.delete(item)       
    session.commit() 






