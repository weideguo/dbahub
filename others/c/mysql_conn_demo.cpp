/*
 * complite:
 * g++ mysql_conn_demo.cpp -o mysql_conn_demo -L/data/hadoop/mysql5530/lib -lmysqlclient 
 * 
 * run:
 * export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/hadoop/mysql5530/lib
 * ./mysql_conn_demo
 *
 */


#include <mysql.h>
#include <string>
#include <iostream>

using namespace std;

int main(int argc,char *argv[])
{
    MYSQL mysql;
    mysql_init(&mysql);
	const char *user="root";
	const char *passwd="";
	const char *host="127.0.0.1";
	unsigned int port=3306;
	const char *db="test";
	const char *sql="select * from a";
    //cout<<sql<<endl;
    	
	//MYSQL mysql;
	MYSQL_RES *result;
	MYSQL_ROW sql_row;
	//int res;
	//mysql_init(&mysql);
    
	if (mysql_real_connect(&mysql, host, user, passwd, db, port, NULL, 0))
	{ 
        //cout<<"xxxxxx"<<endl;
        
		int res=mysql_query(&mysql,sql);
	    //cout<<"res is "+res<<endl;
		if (!res)
		{
			result = mysql_store_result(&mysql);
			if (result)
			{
				while (sql_row = mysql_fetch_row(result))
				{
					cout<<sql_row[0]<<"   "<<sql_row[1]<<endl;
				}	
			}
		}else{

			cout<<"query failed"<<endl;
		}
    
	}else{
	
		cout<<"connect mysql failed"<<endl;
	}
    
	if (result!=NULL)
	{
		mysql_free_result(result);
	}
    try{ 
	   mysql_close(&mysql);
    }catch(const exception& ex){
        cout<<ex.what()<<endl;
    }
    cout<<"close complete"<<endl; 
	return 0;
}	
