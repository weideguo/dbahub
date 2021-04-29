package main

import (
    "fmt"
    "sort"
)

func main(){
	data := []int{10, 25, 11, 26}
	i := sort.Search(len(data), func(i int) bool {
		return data[i] >= 27                           //获取匹配的下标i；如果都不匹配，则为 列表长度+1
	})
	fmt.Println(i)  
}