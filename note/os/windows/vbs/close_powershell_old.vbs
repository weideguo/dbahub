'�ļ�Ӧ�ñ���ΪANSI
'��Ϊ���ڲ���ʹ��powershell���� �ڴ˶�ʱ���ر�powershell 
'wscript.exe �رոĽ��̿ɻָ�����
'��������
On Error Resume Next
'���ȷ��ֻ����һ�Σ�



set wmi=Getobject("winmgmts:\\.\root\cimv2")
Set shell = CreateObject("wscript.shell")




check=MsgBox("�������̨���У�������������������������رն�Ӧ��wscript.exe����",65,"�Ƿ��̨���У�")
if check=1 Then
    Call myTerminate("powershell")
ElseIf check=2 Then
    MsgBox("����������")
End If


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
'�����ɴ˽�������
'Exit sub 
