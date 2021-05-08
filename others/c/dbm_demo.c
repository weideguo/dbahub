
/*
yum install gdbm gdbm-devel
gcc dbm_demo.c -I/usr/include/gdbm -L/usr/lib64/ -lgdbm_compat -lgdbm

kv内存存储
*/

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
//#include <gdbm-ndbm.h>
#include <ndbm.h> 
 

#define TEST_DB_FILE "/tmp/dbm_test"
#define TEST_DB_LEN 3
 
/* 存储的结构体 */
struct test_data {
    char misc_chars[15];
    int  any_integer;
    char more_chars[21];
};
 
int main() {
 
    struct test_data items_to_store[TEST_DB_LEN];
    struct test_data item_retrieved;
 
    char key_to_use[20];
    int i, result;
 
    datum key_datum;
    datum data_datum;
    
    DBM *dbm_ptr;
 
    dbm_ptr = dbm_open(TEST_DB_FILE, O_RDWR | O_CREAT, 0666);
    if (!dbm_ptr) {
        fprintf(stderr, "Failed to open database\n");
        exit(EXIT_FAILURE);
    }
 
    /* put some data in the structures */
    memset(items_to_store, '\0', sizeof(items_to_store));
    
    strcpy(items_to_store[0].misc_chars, "First!");
    items_to_store[0].any_integer = 47;
    strcpy(items_to_store[0].more_chars, "foo");
    
    strcpy(items_to_store[1].misc_chars, "bar");
    items_to_store[1].any_integer = 13;
    strcpy(items_to_store[1].more_chars, "unlucky?");
    
    strcpy(items_to_store[2].misc_chars, "Third");
    items_to_store[2].any_integer = 3;
    strcpy(items_to_store[2].more_chars, "baz");
 
    // 将结构体存储
    for (i = 0; i < TEST_DB_LEN; i++) {
        
        // 构建存储的key的名
        sprintf(key_to_use, "%c%c%d",
            items_to_store[i].misc_chars[0],
            items_to_store[i].more_chars[0],
            items_to_store[i].any_integer);
 
        // key
        key_datum.dptr = (void *)key_to_use;
        key_datum.dsize = strlen(key_to_use);
        // value/data
        data_datum.dptr = (void *)&items_to_store[i];       // 获取结构体指针，即存储的数据为结构体设置的数据
        data_datum.dsize = sizeof(struct test_data);
 
        result = dbm_store(dbm_ptr, key_datum, data_datum, DBM_REPLACE);        // 保存于文件
        
        printf("save kv: %s ,%s %d %s\n", key_to_use, items_to_store[i].misc_chars, items_to_store[i].any_integer, items_to_store[i].more_chars );
        if (result != 0) {
            fprintf(stderr, "dbm_store failed on key: %s\n", key_to_use);
            exit(2);
        }
    } 
    
    printf("now save done, input any keyname to fetch\n");
    
    char key_to_fetch[20];
    scanf("%s", key_to_fetch);
   
    // 读取
    // sprintf(key_to_fetch, "bu%d", 13);   // bu13 查找key名为这个的数据
    
    key_datum.dptr = key_to_fetch;
    key_datum.dsize = strlen(key_to_fetch);
 
    data_datum = dbm_fetch(dbm_ptr, key_datum);
    if (data_datum.dptr) {
        
        memcpy(&item_retrieved, data_datum.dptr, data_datum.dsize);
        printf("retrieved kv: %s, %s %d %s\n",
               key_to_fetch,
               item_retrieved.misc_chars,
               item_retrieved.any_integer,
               item_retrieved.more_chars);
    }
    else {
        printf("no data found for key: %s\n", key_to_fetch);
    }
 
    dbm_close(dbm_ptr);
 
    exit(EXIT_SUCCESS);
}
