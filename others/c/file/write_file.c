#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define true 1
#define false 0

const char *filename = "/tmp/test.txt";

int write_file(const char *message) {

    FILE *file = fopen(filename, "a+");
    if (file == NULL) {
        return false;
    }
    
    if (fwrite(message, sizeof(message), 1, file) <= 0) {
        printf("fwrite error");
    }
    fclose(file);
    return true;
}

int write_file1(const char *message) {

    FILE *file = fopen(filename, "a+");
    if (file == NULL) {
        return false;
    }
    size_t buffer_size = strlen(message) + 20;
    char *buffer = malloc(buffer_size);
    if (buffer == NULL) {
        return false;
    }
    memset(buffer, '\0', buffer_size);
    strcat(buffer, message);
    
    fputs(buffer, file);
   
    free(buffer);
    return true;
}

int main(int argc,char *argv[]){
    char *message;
    message = argv[1];
    write_file1(message);
    
    return 0;
}