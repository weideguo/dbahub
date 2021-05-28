package main

import (
	"fmt"
	"sync"
)

func main() {
    // 相对于普通的map能实现并发安全，普通的map不能并发读写
	var scene sync.Map
    
	scene.Store("greece", 97)
	scene.Store("london", 100)
	scene.Store("egypt", 200)

    v,err := scene.Load("londonx")
	fmt.Println(v,err)

	scene.Delete("london")
   
	scene.Range(func(k, v interface{}) bool {

		fmt.Println("iterate:", k, v)
		return true
	})

}
