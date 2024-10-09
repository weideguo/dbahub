'现定时关闭特定进程
do
set bag=getobject("winmgmts:\\.\root\cimv2")
'set pipe=bag.execquery("select * from win32_process where name like '%QQ%'")
'set pipe=bag.execquery("select * from win32_process where name ='svchost.exe'")
set pipe=bag.execquery("select * from win32_process where name ='powershell.exe'")
            
Set app = CreateObject("wscript.shell")       
for each i in pipe
    '调用命令行杀死进程
    app.run("taskkill /T /F /pid "+CStr(i.ProcessId)) 
    '使用内置函数结束进程 有可能不能杀死            
    i.terminate()
next
wscript.sleep 1000
loop

'查看对象的属性
'For Each objItem In i.Properties_

'查看对象的方法
'For Each objItem In i.methods_
'    'WScript.Echo "Property : "&objItem.name
'next
