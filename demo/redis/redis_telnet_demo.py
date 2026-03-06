import telnetlib
import time


tn = telnetlib.Telnet("10.0.0.1",port=11100)
time.sleep(3)
tn.write("auth my_redis_passwd\n")
time.sleep(3)
tn.write("monitor\n")
time.sleep(60)
tn.write("quit\n")
time.sleep(3)
str_all = tn.read_all()

f = open("redis_monitor.txt", 'w')
f.write(str_all)
f.close()
tn.close()
