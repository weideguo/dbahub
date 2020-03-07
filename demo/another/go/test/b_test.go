package my_test

import "testing"

func TestA(t *testing.T) {
    t.Log("A")
}
func TestAK(t *testing.T) {
    t.Log("AK")
}
func TestB(t *testing.T) {
    t.Log("B")
}
func TestC(t *testing.T) {
    t.Log("C")
}

//只运行特定测试用例
//go test -v -run TestAK b_test.go
