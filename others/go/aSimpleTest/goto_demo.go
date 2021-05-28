
package main

import "fmt"

func f1() {

	for x := 0; x < 10; x++ {

		for y := 0; y < 10; y++ {

			if y == 2 {
				// 跳转到标签
				goto breakHere
			}

		}
	}

	// 手动返回，避免执行进入标签
	return

	// 标签
breakHere:
	fmt.Println("done")
}


func f2() {

OuterLoop:
	for i := 0; i < 2; i++ {
		for j := 0; j < 5; j++ {
			switch j {
			case 2:
				fmt.Println(i, j)
				break OuterLoop
			case 3:
				fmt.Println(i, j)
				break OuterLoop
			}
		}
	}
}

func main(){
    f1()
    f2()
}




