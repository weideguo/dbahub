print "please input a number"
my_int=input()  	###输入数字

print "please input a string"
my_str=raw_input()	###输入字符串
print my_int  			###输出
print my_str



import getpass
#输入的信息不会在命令行显示
sudo_pass = getpass.getpass("What's your sudo password? ")
