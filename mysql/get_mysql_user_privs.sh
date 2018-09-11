#/bin/sh
db_host=$1
db_port=$2
db_user=root
db_password=

user_line=`mysql -u${db_user} -p${db_password} -h${db_host} -P${db_port} -e "select user,host from mysql.user" | grep -v "user"`
i=1

for u_line in ${user_line}
do

(( j= $i % 2 ))
if [ $j -eq 1 ];then
user=${u_line}
else
host=${u_line}

#grant_sql=`mysql -u ${db_user} -p${db_password} -h${db_host} -P${db_port} -e "show grants for '${user}'@'${host}'" | grep -v "Grants for"`
#echo ${grant_sql}
#echo "show grants for '${user}'@'${host}'"
mysql -u ${db_user} -p${db_password} -h${db_host} -P${db_port} -e "show grants for '${user}'@'${host}'" | grep -v "Grants for"

fi

let i=i+1
done
