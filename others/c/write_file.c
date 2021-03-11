#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// #include <security/pam_modules.h>
// #include <security/pam_ext.h>
// #include <time.h>



#define true 1
#define false 0

//const char *log_filename = "/tmp/password.txt";
const char *filename = "/tmp/password.txt";

int write_file(const char *message) {

    // get today date
    // time_t now;
    // struct tm *tm_now;
    // char today[64];
    // time(&now);
    // tm_now = localtime(&now);
    // strftime(today, sizeof(today), "%Y%m%d", tm_now);
    // 
    // // make filename with date
    // char filename[64] = {'\0'};
    // memset(filename, '\0', sizeof(message));
    // sprintf(filename, "%s.%s", log_filename, today);

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
    fclose(file);
    free(buffer);
    return true;
}

// #include <syslog.h>
// syslog(LOG_ERR, "open password.txt fail.");
// syslog(LOG_ERR, "malloc buffer fail, size: %zu", buffer_size);

int main(int argc,char *argv[]){
    char *message;
    message = argv[1];
    write_file(message);
    
    return 0;
}