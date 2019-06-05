cookies
// js 设置cookies
var exp = new Date();
exp.setTime(exp.getTime() + 10000);               //单位为毫秒
exp.toGMTString()
document.cookie="mykey_name=xxx;expires=exp;path=/"  
//expires 过期时间 超过这个时间浏览器不再传这个字段
//path 如果不设置，只能在当前页面获取
//httponly=true 不允许js获取 只允许通过http传输到服务端

//获取
cookie_lenght=document.cookie.length
document.cookie.substring(0,cookie_lenght)


cookie      #缓存在浏览器，每次访问同时时提交指定域的cookie  使用浏览机器时 访问url则该网站的cookie会自动全部提交
            #可以在服务端中设置 通过在response中设置Set-Cookie字段实现
            
session     #服务端设置 


客户端保存与提交机制
[1] 使用cookie来保存。
[2] 使用URL附加信息的方式。（sessionStorage/localStorage等存储，访问时再拼接到url）
[3] 在页面表单里面增加隐藏域。(表单有一行不显示，通过表单提交)
