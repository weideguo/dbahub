package main

//查找当前目录下目录demo下的包
import "./demo"
import . "./demo"


/*

import 引用的位置

1.标准库
  $GOROOT/src     //$GOROOT 默认为安装的根目录 
2.项目的工作目录
    $GOPATH/src     
3.当前目录

可以使用 "." ".."改变目录
*/


func main() {
    // package XXX
    // 指定引用前缀
    demox.PrintStr()
    
    // import . "./demo" 
    // 这种方式引用可以不用加前缀
    PrintStr()
}
