//在js中实现js脚本加载 可用于chrome console的调试
var script = document.createElement('script');
script.src = "https://cdn.bootcss.com/jquery/2.1.2/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script)



const pyodideUrl = "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js";
await import(pyodideUrl);
let pyodide = await loadPyodide();
// 可以直接执行python代码
pyodide.runPython("print('Hello from Python!')");

