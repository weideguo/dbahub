>>time.time()    
1504881596.747973

>>> time.gmtime()
time.struct_time(tm_year=2017, tm_mon=9, tm_mday=8, tm_hour=6, tm_min=51, tm_sec=23, tm_wday=4, tm_yday=251, tm_isdst=0)

>>> time.localtime()
time.struct_time(tm_year=2017, tm_mon=9, tm_mday=8, tm_hour=14, tm_min=51, tm_sec=32, tm_wday=4, tm_yday=251, tm_isdst=0)

>>> time.localtime(0)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)


>>time.asctime(time.localtime())
'Fri Sep  8 14:53:45 2017'

>>> time.ctime()  
'Fri Sep  8 15:01:15 2017'

>>time.ctime(0) 
'Thu Jan  1 08:00:00 1970'


>>time.mktime(time.localtime())
1504853831.0


>> time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
'2017-09-08 14:59:25'


>>time.strptime('2017-09-08 14:59:25','%Y-%m-%d %H:%M:%S')
time.struct_time(tm_year=2017, tm_mon=9, tm_mday=8, tm_hour=14, tm_min=59, tm_sec=25, tm_wday=4, tm_yday=251, tm_isdst=-1)



