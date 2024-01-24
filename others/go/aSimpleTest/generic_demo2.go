package main


import "fmt"

type Numeric interface { 
    float64 | int | int8 | int16 | int32 | int64 | uint | uint8 | uint16 | uint32 | uint64 | uintptr | float32 | complex64 | complex128 | string 
}

func Add[T Numeric](a, b T) T { 
    return a + b
}


func IsListContain[T int | string ](target T, targetArray []T) bool {
    for _, element := range targetArray {
        if target == element {
            return true
        }
    }
    return false
}


func main(){
    fmt.Println(Add(1,2))
    fmt.Println(Add(1.1,2.1))
    fmt.Println(Add("aaa","bbb"))
    fmt.Println(IsListContain("aaa",[]string{"aaa","bbb"}))
    fmt.Println(IsListContain("aaa",[]string{"aad","bbb"}))
    fmt.Println(IsListContain(111,[]int{111,222}))
    fmt.Println(IsListContain(111,[]int{112,222}))
}

