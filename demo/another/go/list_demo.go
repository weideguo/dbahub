package main

import "fmt"
import "container/list"

// 数组
func listTest() {
    var a [4]int
    // 没有赋值的元素默认为0
    a=[4]int{1, 2, 3}
    fmt.Println(a) 
    fmt.Println(a[0])
}

func listTest1() {
    var a [4]string
    a=[4]string{"111", "222", "333"}
    a[3] = "4444"
    for k,v := range a {
        fmt.Println(k,v)
    }    

}
// 多维数组
func listTest2() {
    var a [4][2]int
    // 全量初始化
    // a=[4][2]int{{11,12},{21,22},{31,32},{41,42}}
    // 只是初始化制定索引的元素 索引从1开始
    a=[4][2]int{1:{21,22},3:{31,32}}    
    //对指定元素赋值
    a[0]=[2]int{11,12}
    
    fmt.Println(a)

}


//切片
func listTest3() {
    var a []int
    a=[]int{100,200}
    fmt.Println(a)
    
    //多维切片
    var b [][]int
    b=[][]int{{100},{200,2001}}
    b[0]=append(b[0],3001)
    fmt.Println(b)

}

func listTestx() {
    l := list.New()
    l.PushBack("canon")
    
    for i := l.Front(); i != nil; i = i.Next() {
        fmt.Println(i.Value)
    
    }       
    
}


func main() {
    listTest3()
}
