node.js
实现js在服务端运行

脚本模式
node helloworld.js




交互模式
node进入命令行









JS

变量
var x=var_value;   //变量指定时不需指定类型

数组
var mycars=new Array();
mycars[0]="Saab";
mycars[1]="Volvo";
mycars[2]="BMW";
var mycars2=new Array("Saab","Volvo","BMW");


函数
function function_name(x,y){
return x*y;
}
func1(10,20)    //调用

var doSomething = function(a,b){
 return a + b;
}
doSomething(10,20)   ///调用

回调函数 callback
A callback is a function that is passed as an argument to another function and 
is executed after its parent function has completed.

var doit = function(callback)
{
    var a = 1,
        b = 2,
        c = 3;
    var t = callback(a,b,c);
    return t + 10;
};
var d = doit(function(x,y,z){
    return (x+y+z);
});
console.log(d);

///callback不是关键字，可以任取

调用 doit函数，参数是一个匿名函数；
进入 doit 的函数体中，先定义 a,b,c，然后执行刚才的匿名函数，参数是 a,b,c，
并返回一个 t，最后返回一个 t+10给 d。





eval(string)   //以js命令执行字符串
eval("x=10;y=20;console.log(x*y)")






浏览器的HTML文档  document 对象
document.write(string);   //在浏览器页面写入html代码
document.getElementById("mydiv").innerHTML = "<h>weideguo</h>";   //通过id获取元素在元素中插入html代码  如<div>inner_HTML</div>
document.getElementById("mydiv").setAttribute("style","height:100px;width:965px;background-color:#0000FF;");   		//设置属性
document.getElementById("mydiv").removeAttribute("style","height:100px;width:965px;background-color:#0000FF;");     //删除属性

//getElementsByClassName("myClass") 	 通过类名获取元素   如<div  class="myClass"></div>
//getElementsByName("myInput")        通过名称获取元素   如<input name="myInput" type="text" size="20" />
//getElementsByTagName("div") 		 通过元素类型获取元素 如<div></div>	
//getElementsByTagNameNS				 
document.getElementsByTagName("p")[3];    //获取第4个段落





CSS
//<div id="mydiv" class="myclass" style="height:100px;width:965px;background-color:#0099FF;"></div>
<canvas id="myCanvas"  style="width:200px;height:100px;border:1px solid #c3c3c3;">Your browser does not support the canvas element.</canvas>  //solid 边框颜色  





浏览器窗口 window对象

window.location.host; 		//返回url 的主机部分，例如：www.xxx.com  
window.location.hostname; 	//返回www.xxx.com  
window.location.href; 		//返回整个url字符串(在浏览器中就是完整的地址栏)，例如：www.xxx.com/index.php?class_id=3&id=2  
window.location.pathname; 	//返回/a/index.php或者/index.php  
window.location.protocol; 	//返回url 的协议部分，例如： http:，ftp:，maito:等等。  
window.location.port 		//url 的端口部分，如果采用默认的80端口，那么返回值并不是默认的80而是空字符

window.open("http://www.weideguo.com")   //浏览器新开一个页面访问url




alert(string);        //浏览器中弹出对话框
console.clear();      //chrome控制台中清屏



AJAX
Asynchronous  JavaScript And XML

xmlhttp=new XMLHttpRequest();


//用于和服务器交换数据
xmlhttp.open("GET","demo_get2.asp?fname=Bill&lname=Gates",true);     
//open(method,url,async)  async：true（异步）或 false（同步）
xmlhttp.send();

//POST方法
xmlhttp.open("POST","ajax_test.asp",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("fname=Bill&lname=Gates");

xmlhttp.reponseText;

//responseText	获得字符串形式的响应数据。
//responseXML	获得 XML 形式的响应数据




onreadystatechange	存储函数（或函数名），每当 readyState 属性改变时，就会调用该函数。
readyState	
存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。
0: 请求未初始化
1: 服务器连接已建立
2: 请求已接收
3: 请求处理中
4: 请求已完成，且响应已就绪

xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)   //status	200: "OK"404: 未找到页面
    {
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
  }


//加载xml
function loadXMLDoc(dname) 
{
try //Internet Explorer
  {
  xmlDoc=new ActiveXObject("Microsoft.XMLDOM");
  }
catch(e)
  {
  try //Firefox, Mozilla, Opera, etc.
    {
    xmlhttp=document.implementation.createDocument("","",null);
    }
  catch(e) {alert(e.message)}
  }
try 
  {
  xmlhttp.async=false;
  xmlhttp.load(dname);
  return(xmlhttp);
  }
catch(e) {alert(e.message)}
return(null);
}

var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }







