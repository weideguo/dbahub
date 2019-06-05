
browser对象
// Window 对象表示浏览器中打开的窗口。 如果文档包含框架（<frame> 或 <iframe> 标签），浏览器会为 HTML 文档创建一个 window 对象，并为每个框架创建一个额外的 window 对象。
// Navigator 对象包含有关浏览器的信息
// Screen 对象包含有关客户端显示屏幕的信息
// History 对象包含用户（在浏览器窗口中）访问过的 URL。 History 对象是 window 对象的一部分，可通过 window.history 属性对其进行访问。
// Location 对象包含有关当前 URL 的信息。Location 对象是 window 对象的一部分，可通过 window.Location 属性对其进行访问。
// 存储对象
// localStorage 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去除。
// sessionStorage 用于临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据。


window.location.host; 		//返回url 的主机部分，例如：www.xxx.com  
window.location.hostname; 	//返回www.xxx.com  
window.location.href; 		//返回整个url字符串(在浏览器中就是完整的地址栏)，例如：www.xxx.com/index.php?class_id=3&id=2  
window.location.pathname; 	//返回/a/index.php或者/index.php  
window.location.protocol; 	//返回url 的协议部分，例如： http:，ftp:，maito:等等。  
window.location.port 		//url 的端口部分，如果采用默认的80端口，那么返回值并不是默认的80而是空字符

window.open("http://www.weideguo.com")   //浏览器新开一个页面访问url
