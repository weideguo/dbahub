package main

import "fmt"

func f() {
    fmt.Printf("i am f() \n" )
}

// 函数存在返回值 需要在声明指定返回值类型
func f1(x int) int {
    return x
}

// 函数可以返回多个值
func f2(x int, y string) (int,string) {
    // a,b := x,y
    return x,y
}

func f3(x int,y string) (a int,b string) {
    a=x
    b=y
    // 对返回值命令是return 可以选择不填返回列表
    // return a,b
    return
}

// 返回值在函数没有赋值时 使用默认值返回
// int 0
// string ""
// bool false 
func f4(x int) (a string) {
    return 
}

// 指针
// *string 
// *int       
func f5(x string)(y *string){
    // & 取得地址符号
    a := &x    
    return a
}


// 主函数进入程序   
// main 不能有参数以及返回值
func main() {
    // f()
    
    // a := f1(100)
    // fmt.Printf("%d \n" , a)
    
    /*
    b,c := f2(1,"yyy")
    fmt.Printf("%d \n" , b)
    fmt.Printf("%ds \n" , c)
    */

    /*
    d,e := f3(1,"yyy")
    fmt.Printf("%d \n" , d)
    fmt.Printf("%s \n" , e)
    */
    
    // f := f4(1)
    // fmt.Printf("%d \n" , f) 

    g :=f5("aaa")
    fmt.Printf("%p \n" , g)
    // 查看指针类型
    fmt.Printf("type: %T\n", g)
    // 取指针值
    fmt.Printf("%s \n" , *g)
    
    
}


