package main


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
