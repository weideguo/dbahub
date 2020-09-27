cookies
// js 设置cookies
var exp = new Date();
exp.setTime(exp.getTime() + 10000);               
document.cookie="mykey_name=xxx;expires="+exp.toGMTString()+";path=/"  
//expires 过期时间 超过这个时间浏览器不再传这个字段  单位为毫秒
//max-age 保存的时间 优先级高于expires 秒
//path 如果不设置，只能在当前页面获取
//httponly=true 不允许js获取 只允许通过http传输到服务端

//获取
cookie_lenght=document.cookie.length
document.cookie.substring(0,cookie_lenght)

//cookie没有删除方法 通过重置其expires时间实现删除

// 获取指定key的值
function getCookie(name){
  let arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
  if (arr != null) return unescape(arr[2]); 
  return null;
}

headers的key和值不区分大小写
cookie      #缓存在浏览器，每次访问同时时提交指定域的cookie  使用浏览机器时 访问url则该网站的cookie会自动全部提交
            #请求时由headers的Cookie携带
            #响应时设置headers的Set-Cookie字段，浏览器获取后自动设置成cookie
            
session     #服务端的封装 在前端都是通过cookie存储，后端再存储一份，用于登陆的验证





客户端保存与提交机制
[1] 使用cookie来保存。
[2] 使用URL附加信息的方式。（sessionStorage/localStorage等存储，访问时再拼接到url）
[3] 在页面表单里面增加隐藏域。(表单有一行不显示，通过表单提交)


// localStorage   不自动清理
// sessionStorage 关会话即清理
localStorage.setItem(key,value);    // 保存数据
localStorage.getItem(key);          // 读取数据
localStorage.removeItem(key);       // 删除单个数据 
localStorage.clear();               // 删除所有数据 
localStorage.key(index);            // 得到某个索引的key
