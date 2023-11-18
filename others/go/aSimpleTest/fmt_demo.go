package main

import (
    "fmt"
)

type point struct {
    x, y int
}

func main(){

    fmt.Println("%s 输出字符串")
    fmt.Printf("%s-%s-%s\n","I","am","xxx")
    
    fmt.Println("%c Unicode 码转字符")
    fmt.Printf("%c\n",97)
    fmt.Printf("%c\n",10000)
    fmt.Printf("%c\n",0x97E6)
    
    fmt.Println("%q Unicode 码转字符，有单引号")
    // fmt.Printf("%q\n","hello")
    fmt.Printf("%q\n",97)
    fmt.Printf("%q\n",10000)
    fmt.Printf("%q\n",0x97E6)
    
    fmt.Println("%U Unicode")
    fmt.Printf("%U\n",0x97E6)
    fmt.Printf("%#U\n",0x97E6)


    // 有符号十进制整数(int)（%ld、%Ld：长整型数据(long),%hd：输出短整形。）
    fmt.Println("%d 输出十进制")
    fmt.Printf("%d\n", 110)
    
    fmt.Println("%x 输出十六进制，非数字则为对应ascii的16进制")
    fmt.Printf("%x\n", 10)     //a
    fmt.Printf("%x\n", "abcz")
    
    fmt.Printf("%X\n", 10)    // A
    fmt.Printf("%#X\n", 10)   // 0XA
    

    fmt.Println("%o 输出八进制")
    fmt.Printf("%o,%o,%o\n", 10, 010, 0x10)
    
    fmt.Println("%b 输出二进制")
    fmt.Printf("%b\n", 110)

    
    fmt.Println("%f 输出浮点型数值")
    fmt.Printf("%f\n", 27.89)


    
    // 控制输出的宽度，默认右对齐的，左边加上空格
    fmt.Println("控制输出的宽度和精度")
    fmt.Printf("|%5d|%5d|\n", 12, 345)
    fmt.Println("输出宽度，同时指定浮点数")
    fmt.Printf("|%5.2f|%5.2f|\n", 1.2, 3.45)
    fmt.Println("左对齐")
    fmt.Printf("|%-5.2f|%-5.2f|\n", 1.2, 3.45)
    
    
    fmt.Println("%t 布尔占位符")
    fmt.Printf("%t\n", true)
    
    
    p := point{1, 2}

    fmt.Println("%p 输出一个指针的值")
    fmt.Printf("%p\n", &p)
    fmt.Println("%v 输出结构体的对象值")
    fmt.Printf("%v\n", p)
    
    fmt.Println("%+v 输出结构体的成员名称和值")
    fmt.Printf("%+v\n", p)
    fmt.Println("%#v 输出一个值的Go语法表示方式")
    fmt.Printf("%#v\n",p)
    fmt.Println("%T 输出一个值的数据类型")
    fmt.Printf("%T\n",p)
    
    fmt.Println("科学计数 %b 2为底；%e 10为底")
    fmt.Printf("%b\n", 0.1)
    
    fmt.Printf("%e\n", 10.2)
    fmt.Printf("%E\n", 10.2)
    
}