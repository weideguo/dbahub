'文件应该保存为ANSI
'因为存在病毒使用powershell启动 在此定时检查关闭powershell 
'wscript.exe 关闭改进程可恢复正常
'跳过错误
On Error Resume Next

set wmi=Getobject("winmgmts:\\.\root\cimv2")
Set shell = CreateObject("wscript.shell")

pidFile=split(Wscript.ScriptFullName,".vbs")(0)+".pid"

Set fso =CreateObject("Scripting.FileSystemObject")
pid=fso.OpenTextFile(pidFile).ReadLine
if pid > 0 Then
    MsgBox("进程已经存在，请检查进程号: "+pid)
Else
    pid = CurrProcessId(shell,wmi)
    check=MsgBox("将进入后台运行，如需结束，请进入任务管理器关闭对应的wscript.exe进程，或者关闭进程 " & pid,65,"是否后台运行？")
    if check=1 Then
        Set a = fso.CreateTextFile(pidFile, True)
        a.WriteLine(pid)
        a.Close
        Call myTerminate("powershell")
    ElseIf check=2 Then
        shell.PopUp "将结束进程,10s后自动关闭",10,"结束进程"
    End If  
End if


Function CurrProcessId(shell,wmi)
    sCmd = "/K " & Left(CreateObject("Scriptlet.TypeLib").Guid, 38)
    '运行cmd
    shell.Run "%comspec% " & sCmd, 0
    Set ChildrenProcess = wmi.ExecQuery("Select * From Win32_Process Where CommandLine Like '%" & sCmd & "'",,32)
    For Each c In ChildrenProcess
        pid = c.ParentProcessId
        c.Terminate
        Exit For
    Next
    CurrProcessId = pid
End Function


Sub myTerminate(process_name)
    do
        set pipe=wmi.execquery("select * from win32_process where name like '%"+process_name+"%'")
        for each i in pipe
            shell.run("taskkill /T /F /pid "+CStr(i.ProcessId))
            i.terminate()
        next
        wscript.sleep 2000
    loop
End sub

'Sub没有返回值 Function有返回值
'结束
'Exit sub 
