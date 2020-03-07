package main

import "fmt"

//变长参数
func f(nums ...int){
    fmt.Println(nums)
    //可以直接当初数组使用
    fmt.Println(nums[0])
}


func main(){
    f(51,2,3,4)
}
