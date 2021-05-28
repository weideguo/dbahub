'文件应该保存为ANSI
'因为存在病毒使用powershell启动 在此定时检查关闭powershell 
'wscript.exe 关闭改进程可恢复正常
'跳过错误
'On Error Resume Next

set wmi=Getobject("winmgmts:\\.\root\cimv2")
Set shell = CreateObject("wscript.shell")

pidFile=split(Wscript.ScriptFullName,".vbs")(0)+".pid"

Set fso =CreateObject("Scripting.FileSystemObject")

call startProcess

Sub startProcess()
    check=MsgBox("将进入后台运行，如需结束，请进入任务管理器关闭对应的wscript.exe进程，或者关闭进程 " & pid,65,"是否后台运行？")
    if check=1 Then
        do
            On Error Resume Next
            processListFile=split(Wscript.ScriptFullName,".vbs")(0)+".txt"
            Set f = fso.OpenTextFile(processListFile)
            do until f.atendofstream
                processname=Trim(f.readline)
                if not processname ="" And not regCheck("^#.*$", processname) Then
                    Call myTerminate(processname)
                End If
            loop
        loop 
    ElseIf check=2 Then
        shell.PopUp "将结束进程,10s后自动关闭",10,"结束进程"
    End If  
End sub

function regCheck(pattern,str)    
    set re=new regexp 
    re.global=true 
    re.ignorecase=true 
    re.pattern=pattern   
    regCheck=re.test(str) 
end function 

Sub myTerminate(process_name)
    set pipe=wmi.execquery("select * from win32_process where name like '"+process_name+"'")
    for each i in pipe
        'wscript.echo i.ProcessId
        '需要在admin账号下运行才行 否则没有权限杀死一些进程
        shell.run("taskkill /F /pid "+CStr(i.ProcessId))
        i.terminate()
    next
    wscript.sleep 200
End sub

'Sub没有返回值 Function有返回值
'结束
'Exit sub 
