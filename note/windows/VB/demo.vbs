'vb不区分大小写 关键字使用风格为首字母大写
wscript.sleep(3000)

'弹出框
MsgBox("yyyy")
wscript.Echo("xxx")

'创建 ActiveX 对象
'COM（组件对象模型）
'Scripting.FileSystemObject、WScript.Shell、ADODB.Stream
Set app = CreateObject("wscript.shell")

'vbs中不能使用shell函数
'Dim MyAppID, ReturnValue
'ReturnValue = Shell("C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")


'AppActivate用于激活某一已经运行的应用程序窗口
'app.AppActivate("微信")
'app.AppActivate(ReturnValue)


'需要预先设置环境变量 确保在命令行中能直接运行命令
'app.run "WeChat"


'循环
'For i=0 To 10
'xxx
'Next

'向活动的窗口发送消息 运行vb后选中窗口
'SHIFT + 
'CTRL  ^ 
'ALT % 

'CTRL + v
'app.SendKeys "^v"

'只能模拟键盘的字符 不能输入中文等字符
app.SendKeys "nihaoa"

wscript.sleep(1000)
'空格键
app.sendkeys " "


'回车
'app.sendkeys "{ENTER}"

'ALT + s  微信PC版本中的发送
app.SendKeys "%s"

'alt +f4 关闭窗口
app.SendKeys "%{F4}"

