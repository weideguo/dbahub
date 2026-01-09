windows下
``` bat
:: 编译
set GOOS=js 
set GOARCH=wasm 
go build -o main.wasm main.go

:: 复制golang对wasm支持的js
go env GOROOT
cp "上述目录\lib\wasm\wasm_exec.js" .

:: 使用python启动一个简易web服务
python -m http.server  8123
```

