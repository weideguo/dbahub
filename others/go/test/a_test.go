package my_test

import "testing"

func TestHelloWorld(t *testing.T) {
    t.Log("hello world")
}

/*
单元测试（unit testing），是指对软件中的最小可测试单元进行检查和验证。对于单元测试中单元的含义，一般要根据实际情况去判定其具体含义，如C语言中单元指一个函数，Java 里单元指一个类，图形化的软件中可以指一个窗口或一个菜单等。总的来说，单元就是人为规定的最小的被测功能模块。

测试的函数
func TestXXX( t *testing.T )
文件
*_test.go
运行
go test a_test.go
go test -v a_test.go
*/

/*
Log     打印日志，同时结束测试
Logf    格式化打印日志，同时结束测试
Error   打印错误日志，同时结束测试
Errorf  格式化打印错误日志，同时结束测试
Fatal   打印致命日志，同时结束测试
Fatalf  格式化打印致命日志，同时结束测试
*/
