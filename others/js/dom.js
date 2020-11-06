#DOM对象 Document Object Mode

document.write(string);                                                                                          //在浏览器页面写入html代码
document.getElementById("mydiv").innerHTML = "<h>weideguo</h>";                            //通过id获取元素在元素中插入html代码  如<div>inner_HTML</div>
document.getElementById("mydiv").setAttribute("style","height:100px;width:965px;background-color:#0000FF;");   		//设置属性
document.getElementById("mydiv").removeAttribute("style","height:100px;width:965px;background-color:#0000FF;");     //删除属性

document.getElementsByClassName("myClass") 	  //通过类名获取元素         如<div  class="myClass"></div>
document.getElementsByName("myInput")            //通过名称获取元素       如<input name="myInput" type="text" size="20" />
document.getElementsByTagName("div") 		      //通过元素类型获取元素 如<div></div>	
document.getElementsByTagNameNS(ns,name)				 



