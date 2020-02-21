package main

/*
下载mysql的驱动到 /data/gopath/src
设置环境变量 export GOPATH=/data/gopath

import _ 匿名导入包——只导入包但不使用包内类型和数值
*/
import _ "github.com/go-sql-driver/mysql"
import "fmt"
import "database/sql"

func conn_demo(){
    db_type := "mysql"
    // [username[:password]@][protocol[(address)]]/dbname[?param1=value1&...&paramN=valueN]
    dsn :="root@(127.0.0.1:1039)/test"
    db, err := sql.Open(db_type, dsn)
    fmt.Println(db, err)
}

func main() {
    conn_demo()
}
