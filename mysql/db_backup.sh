#!/bin/bash
# update by dba@wdg in 20170713


shellpath=$(cd "$(dirname "$0")";pwd)
cd ${shellpath}

#build db pair config
#/bin/sh get_slave.sh 

ymd=`date '+%Y%m%d'`
ymdhm=`date '+%Y%m%d%H%M'`

bak_dir="/data/db_user00/daysbackup/"
db_pair_list=`cat full_list | grep -v "^#"`

backup_per_instance()
{

	db_pair=$1	
	dbip=`echo ${db_pair}|awk -F'|' '{print $1}'`
	dbport=`echo ${db_pair}|awk -F'|' '{print $2}'`
	dbuser=`echo ${db_pair}|awk -F'|' '{print $3}'`
	dbpd=`echo ${db_pair}|awk -F'|' '{print $4}'`
	dbmip=`echo ${db_pair}|awk -F'|' '{print $5}'`
	dbmport=`echo ${db_pair}|awk -F'|' '{print $6}'`
	
	base_dir="${bak_dir}/${dbmip}-${dbmport}/${ymd}"

	if [ ! -d ${base_dir} ];then
        	mkdir -p ${base_dir}
	fi
		
	db_list=`mysql -u${dbuser} -p${dbpd} -h${dbip} -P${dbport} -e "show databases;" | grep -Evw 'Database|test|mysql|performance_schema|information_schema'`
		
	for db in ${db_list}
	do
		bak_file="${base_dir}/${db}_${ymdhm}.sql"
		mysqldump --triggers -R --single-transaction --default-character-set=utf8 -u${dbuser} -p${dbpd} -h${dbip} -P${dbport} ${db} > ${bak_file} 2>/dev/null
	
		dump_ok=`tail -n 1 ${bak_file} |grep 'Dump completed on' |wc -l`
		dump_ok2=`tail -n 1 ${bak_file} |grep 'Dump completed on'`
		
		if [ ${dump_ok} -le 1 ];then
			echo "[INFO] ${dump_ok2} + ${db}_${ymdhm}_${dbmip}_${dbmport} "
		else
			echo "[Error] DB_BACKUP is bad: ${db}_${ymdhm}_${dbmip}_${dbmport} " 
		fi	
		#gzip ${bak_file} &
	done
}

compress_file()
{
	db_pair=$1
	dbmip=`echo ${db_pair}|awk -F'|' '{print $5}'`
	dbmport=`echo ${db_pair}|awk -F'|' '{print $6}'`
	bak_files="${bak_dir}/${dbmip}-${dbmport}/${ymd}/*"

	gzip ${bak_files}

}


##########################backup#########################
echo "#### DB BACKUP REPORT IN ${ymdhm} ####"

#thread control
v_thread=5
v_fifofile="/tmp/$$.fifo"
mkfifo -m 700 ${v_fifofile}
exec 6<>${v_fifofile}
rm -rf ${v_fifofile}
###############

for ((k=1;k<=${v_thread};k++));do
	echo >&6
done

for db_pair in ${db_pair_list}
do
	read -u6
	{
		backup_per_instance $db_pair
		echo >&6
	}&
done

##thread control
wait
exec 6>&-
exec 6<&-

########################backup###########################

##################compress###############################

c_thread=2
c_fifofile="/tmp/$$.fifo"
mkfifo -m 700 ${c_fifofile}
exec 7<>${c_fifofile}
rm -rf ${c_fifofile}

for ((k=1;k<=${c_thread};k++));do
        echo >&7
done


for db_pair in ${db_pair_list}
do
	read -u7
	{
		compress_file $db_pair
		echo >&7
	}&
done

wait
exec 7>&-
exec 7<&-


###############compress#################################
echo "#### ENDING ####" 

###delete old backup file
#find ${bak_dir}/*/* -ctime +14 -type d -exec rm -rf {} \;
find -L /data/db_user00/daysbackup/*/* -maxdepth 0 -ctime +35 -type d -exec rm -rf {} \;

