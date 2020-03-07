package my_test

import "testing"
func Benchmark_Add(b *testing.B) {
    var n int
    for i := 0; i < b.N; i++ {
        n++
    }
}

/*
基准测试 测试一段程序的运行性能及耗费 CPU 的程度

函数需要以Benchmark_开头

运行
go test -v -bench=. benchmark_test.go
只运行指定函数
go test -v -bench=Add benchmark_test.go

-benchmem     显示内存分配情况
-benchtime=5s 基准测试框架对一个测试用例的默认测试时间是 1 秒，控制testing.B 中的 N 值
*/
