#define INSERT_QUERY "INSERT INTO test_long_data(text_column) VALUES(?)"
/*
预先创建表
--create table test_long_data(text_column text);
create table test_long_data(text_column varchar(100));

编译
gcc -L/data/mariadb1039/lib/ -lmysqlclient -I/usr/include/mysql/ mysql_stmt_demo.c -o mysql_stmt_demo

执行
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/mariadb1039/lib/ 
./mysql_stmt_demo

*/

#include <stdio.h>
#include <mysql.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc,char *argv[])
{ 
    MYSQL_BIND bind[1];
    long       length;
    MYSQL_STMT *stmt;
    
    MYSQL mysql;
    mysql_init(&mysql);
	const char *user="root";
	const char *passwd="";
	const char *host="127.0.0.1";
	unsigned int port=1039;
	const char *db="test";
    
    if (!mysql_real_connect(&mysql, host, user, passwd, db, port, NULL, 0))
	{ 
        fprintf(stderr, " mysql connect failed\n");
        exit(0);
    }
    
    stmt = mysql_stmt_init(&mysql);
    if (!stmt)
    {
        fprintf(stderr, " mysql_stmt_init(), out of memory\n");
        exit(0);
    }
    /**/
    if (mysql_stmt_prepare(stmt, INSERT_QUERY, strlen(INSERT_QUERY)))
    {
        fprintf(stderr, "\n mysql_stmt_prepare(), INSERT failed");
        fprintf(stderr, "\n %s", mysql_stmt_error(stmt));
        exit(0);
    }
    memset(bind, 0, sizeof(bind));
    
    /////////////////////////////////////////////////////////////////////////////////////
    bind[0].buffer_type= MYSQL_TYPE_STRING;
    bind[0].length= &length;
    bind[0].is_null= 0;
    
    /* 绑定参数到sql */
    if (mysql_stmt_bind_param(stmt, bind))
    {
        fprintf(stderr, "\n param bind failed");
        fprintf(stderr, "\n %s", mysql_stmt_error(stmt));
        exit(0);
    }
    
    /* 
        发送数据（即绑定后的sql的第一部分）给mysql服务器 
        mysql服务器的max_allowed_packet参数控制单次可以发送的最大值
        my_bool mysql_stmt_send_long_data(MYSQL_STMT *stmt, unsigned int parameter_number, const char *data, unsigned long length)
        “parameter_number”指明了与数据关联的参数。参数从0开始编号。“data”是指向包含将要发送的数据的缓冲区的指针，“length”指明了缓冲区内的字节数。
    */
    if (mysql_stmt_send_long_data(stmt,0,"MySQL",5))
    {
        fprintf(stderr, "\n send_long_data failed1");
        fprintf(stderr, "\n %s", mysql_stmt_error(stmt));
        exit(0);
    }
    
    /* 再次发送第二部分数据（即绑定后的sql的第二部分）给mysql服务器 */
    if (mysql_stmt_send_long_data(stmt,0," - The most popular Open Source database",40))
    {
        fprintf(stderr, "\n send_long_data failed2");
        fprintf(stderr, "\n %s", mysql_stmt_error(stmt));
        exit(0);
    }
    
    //// 发送的数据量比较小时，可以不比先调用 mysql_stmt_send_long_data //////////////////////////////////////
    // int STRING_SIZE=50;
    // char          str_data[STRING_SIZE];
    // unsigned long str_length;
    // my_bool       is_null;
    // 
    // bind[0].buffer_type= MYSQL_TYPE_STRING;
    // bind[0].buffer= (char *)str_data;
    // bind[0].buffer_length= STRING_SIZE;
    // bind[0].is_null= &is_null;
    // bind[0].length= &str_length;
    // 
    // 
    // strncpy(str_data, "The most popular Open Source database", STRING_SIZE);
    // str_length= strlen(str_data);    
    // is_null= 0;   
    // 
    // /* 绑定参数到sql */
    // if (mysql_stmt_bind_param(stmt, bind))
    // {
    //     fprintf(stderr, "\n param bind failed");
    //     fprintf(stderr, "\n %s", mysql_stmt_error(stmt));
    //     exit(0);
    // }
    
    
    /* 执行 */
    if (mysql_stmt_execute(stmt))
    {
        fprintf(stderr, "\n mysql_stmt_execute failed");
        fprintf(stderr, "\n %s", mysql_stmt_error(stmt));
        exit(0);
    }
    if (mysql_stmt_close(stmt))
    {
        fprintf(stderr, " failed while closing the statement\n");
        fprintf(stderr, " %s\n", mysql_stmt_error(stmt));
        exit(0);
    }
    mysql_close(&mysql);
}