#include <stdio.h>
#include <stdlib.h>

/*
两阶段写测试
*/

const char *filename = "/tmp/test.txt";
const char str[] = "hello 1234567890\n";

int write_file(const char *message) {
    FILE *fp = fopen(filename, "w");
        
    if (fwrite(str, sizeof(str), 1, fp) <= 0) {
        printf("fwrite error");
    }
    fflush(fp);            
    fsync(fileno(fp));     
        
    char str1[5];
    printf("any input %d chars to continue \n", sizeof(str1));
    scanf("%s", str1);    
    
    fseek(fp, 2, SEEK_SET);
    if (fwrite(str1, sizeof(str1), 1, fp) <= 0) {
        printf("fwrite error2");
    }
    
    fflush(fp);            
    fsync(fileno(fp)); 
    
    fclose(fp);
}

int main(int argc,char *argv[]){
    char *message;
    message = argv[1];
    write_file(message);
    
    return 0;
}

