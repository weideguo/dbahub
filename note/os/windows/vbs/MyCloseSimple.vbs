'�ļ�Ӧ�ñ���ΪANSI
'��Ϊ���ڲ���ʹ��powershell���� �ڴ˶�ʱ���ر�powershell 
'wscript.exe �رոĽ��̿ɻָ�����
'��������
'On Error Resume Next

set wmi=Getobject("winmgmts:\\.\root\cimv2")
Set shell = CreateObject("wscript.shell")

pidFile=split(Wscript.ScriptFullName,".vbs")(0)+".pid"

Set fso =CreateObject("Scripting.FileSystemObject")

call startProcess

Sub startProcess()
    check=MsgBox("�������̨���У�������������������������رն�Ӧ��wscript.exe���̣����߹رս��� " & pid,65,"�Ƿ��̨���У�")
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
        shell.PopUp "����������,10s���Զ��ر�",10,"��������"
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
        '��Ҫ��admin�˺������в��� ����û��Ȩ��ɱ��һЩ����
        shell.run("taskkill /F /pid "+CStr(i.ProcessId))
        i.terminate()
    next
    wscript.sleep 200
End sub

'Subû�з���ֵ Function�з���ֵ
'����
'Exit sub 
