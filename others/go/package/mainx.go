// 通过包名引用包下的对象
import "fmt"
fmt.Println("xxx")


// 更改包名，使用新包名引用
import x "fmt"
x.Println("xxx")


// 引入包的所有对象 使用时不必再加前缀
import . "fmt"
Println("xxx")


import _ "github.com/go-sql-driver/mysql"
/*
操作其实只是引入该包。
当导入一个包时，它所有的init()函数就会被执行，但有些时候并非真的需要使用这些包，仅仅是希望它的init()函数被执行而已。
即使用 _ 操作引用包是无法通过包名来调用包中的导出函数，而是只是为了简单的调用其init函数()。
*/

/*
目录名demo，目录下的文件头为： 
package demox
*/
// import使用目录名
import "demo"
//调用使用package指定的名字
demox.AAA()
