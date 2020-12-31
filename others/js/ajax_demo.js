// AJAX  Asynchronous  JavaScript And XML  //js服务器交换数据


/////////////////////////////////////////////////////////////////////////////////////////////////////////

var xmlhttp;

xmlhttp=new XMLHttpRequest();                    //window.XMLHttpRequest
// xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");  //IE old

xmlhttp.open("GET","https://some_host/demo_get?p1=111&p2=222",true);    // 服务端需要设置headers Access-Control-Allow-Origin:*
//open(method,url,async)  async：true（异步）或 false（同步）
xmlhttp.send();

//POST方法
xmlhttp.open("POST","https://some_host/demo_post",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");  //设置headers
xmlhttp.send("fname=Bill&lname=Gates");


/*
onreadystatechange	存储函数（或函数名），每当 readyState 属性改变时，就会调用该函数。
readyState	
存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。
0: 请求未初始化
1: 服务器连接已建立
2: 请求已接收
3: 请求处理中
4: 请求已完成，且响应已就绪
*/
// 必须通过此实现对返回结果的调用
xmlhttp.onreadystatechange=function(){
    if (xmlhttp.readyState==4 && xmlhttp.status==200){  
        document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
}

//responseText	获得字符串形式的响应数据。
//responseXML	  获得 XML 形式的响应数据





/////////////////////////////////////////////////////////////////////////////////////////////////////////
fetch api 新的后端请求接口，用于替代XMLHttpRequest
url="https://www.baidu.com"
fetch(url)
.then((res)=>{
    console.log(res)
})
.catch((err)=>{
   console.log(err) 
})



var form = new FormData(document.getElementById('login-form'));
fetch("/login", {
  method: "POST",
  body: form
});


// json 上传
var url = 'https://example.com/profile';
var data = {username: 'example'};

fetch(url, {
  method: 'POST',                   // or 'PUT'
  body: JSON.stringify(data), 
  headers: new Headers({
    'Content-Type': 'application/json'
  })
}).then(res => res.json())
.catch(error => {console.error('Error:', error)})
.then(response => {console.log('Success:', response)});



// 文件上传
var formData = new FormData();
var fileField = document.getElementById("inputForm");  // 通过input获取文件
file = fileField.files[0]

formData.append('username', 'abc123');
formData.append('file', file);

fetch('https://example.com/profile/avatar', {
  method: 'PUT',
  body: formData
})
.then(response => response.json())
.catch(error => console.error('Error:', error))
.then(response => console.log('Success:', response));


// header
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");

