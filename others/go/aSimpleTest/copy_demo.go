package main

import "fmt"

func main() {
    // a := [4]int{1, 2, 3}
    // var b [4]int        // 使用这种方式声明则不能用于slice？
    // b[0] =101
    // fmt.Println(b) 
    
    const elementCount = 10
    
	a := make([]int, elementCount)
    
	for i := 0; i < elementCount; i++ {
		a[i] = i
	}
    
    b := make([]int, elementCount)
    
    copy(b, a[2:4]) 
    b[0]=100
    
    // 直接等值则在修改b时会影响a的数据
    // b=a[2:4]
    // b[0]=100
    
    fmt.Println(a)
    fmt.Println(b)
    
}