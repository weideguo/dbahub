#include <mysql.h>  
  
extern "C" {

my_bool testadd_init(UDF_INIT *initid, UDF_ARGS *args, char *message)          
{
    return 0;
}


long long testadd(UDF_INIT *initid, UDF_ARGS *args, char *is_null, char *error)  
{  
    int a = *((long long *)args->args[0]);  
    int b = *((long long *)args->args[1]);  
    return a + b;  
}  
  
}
