Set WSHShell = WScript.CreateObject("WScript.Shell") 
p = "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoDriveTypeAutoRun"
'读取注册表
n = WSHShell.RegRead(p)
MsgBox(n)
'修改注册表
'键 值 键的类型
'RegWrite(strName, anyValue [,strType])
'WSHShell.RegWrite p, n, itemtype 
