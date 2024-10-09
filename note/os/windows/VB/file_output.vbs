'写入文件
Set fso =CreateObject("Scripting.FileSystemObject")
Set a = fso.CreateTextFile("./process.txt", True)

a.WriteLine('single line content')

a.Close
