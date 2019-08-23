'文件应该保存为ANSI
'因为存在病毒使用powershell启动 在此定时检查关闭powershell 
'wscript.exe 关闭改进程可恢复正常
'跳过错误
On Error Resume Next
'如何确定只启动一次？

check=MsgBox("将进入后台运行，如需结束，请进入任务管理器关闭对应的wscript.exe进程",65,"是否后台运行？")
if check=1 Then
    Call myTerminate("powershell")
ElseIf check=2 Then
    MsgBox("将结束进程")
End If

Sub myTerminate(process_name)
    do
        set bag=getobject("winmgmts:\\.\root\cimv2")
        set pipe=bag.execquery("select * from win32_process where name like '%"+process_name+"%'")
        Set app = CreateObject("wscript.shell")
        for each i in pipe
            app.run("taskkill /T /F /pid "+CStr(i.ProcessId))
            i.terminate()
        next
        wscript.sleep 2000
    loop
End sub
'可以由此结束进程
'Exit sub 
