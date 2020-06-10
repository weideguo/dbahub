package main
/*
解析sql文件成抽象语法树
*/
import (
	"fmt"
	"github.com/pingcap/parser"
	_ "github.com/pingcap/tidb/types/parser_driver"
)

func example() {
	p := parser.New()

	stmtNodes, _, err := p.Parse("select * from tbl where id = 1", "", "")

	fmt.Println(stmtNodes[0], err)
}