import os

os.system(r'cls')    	###windows执行系统命令
os.system('clear')		###linux命令行清屏


#slave_IP=os.system(get_ip_cmd)
#slave_IP=commands.getstatusoutput(get_ip_cmd)
#slave_IP=commands.getoutput(get_ip_cmd)
p0=os.popen(get_ip_cmd)
p0.read()

#以后使用代替
import subprocess
r=subprocess.Popen("ls",shell=True,stdout=subprocess.PIPE)
print r.communicate()  #返回值

'''
常用命令执行如果只是判断执行成功与否直接os.system
如果需要拿到输出值 os.popen
非常复杂的情况用 subprocess 
但是谨慎使用管道	???
'''



import sys
args=sys.argv    #使用sys模块，在运行脚本时可传入参数;可以选择 argv[x] 获取第x个参数
			

#获取文件的绝对路径
os.path.dirname(os.path.abspath(__file__))
