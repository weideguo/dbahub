'�ļ�Ӧ�ñ���ΪANSI
'��Ϊ���ڲ���ʹ��powershell���� �ڴ˶�ʱ���ر�powershell 
'wscript.exe �رոĽ��̿ɻָ�����
'��������
On Error Resume Next

set wmi=Getobject("winmgmts:\\.\root\cimv2")
Set shell = CreateObject("wscript.shell")

pidFile=split(Wscript.ScriptFullName,".vbs")(0)+".pid"

Set fso =CreateObject("Scripting.FileSystemObject")
pid=fso.OpenTextFile(pidFile).ReadLine
if pid > 0 Then
    MsgBox("�����Ѿ����ڣ�������̺�: "+pid)
Else
    pid = CurrProcessId(shell,wmi)
    check=MsgBox("�������̨���У�������������������������رն�Ӧ��wscript.exe���̣����߹رս��� " & pid,65,"�Ƿ��̨���У�")
    if check=1 Then
        Set a = fso.CreateTextFile(pidFile, True)
        a.WriteLine(pid)
        a.Close
        Call myTerminate("powershell")
    ElseIf check=2 Then
        shell.PopUp "����������,10s���Զ��ر�",10,"��������"
    End If  
End if


Function CurrProcessId(shell,wmi)
    sCmd = "/K " & Left(CreateObject("Scriptlet.TypeLib").Guid, 38)
    '����cmd
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

'Subû�з���ֵ Function�з���ֵ
'����
'Exit sub 
