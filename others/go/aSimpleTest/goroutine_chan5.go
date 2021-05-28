package main

import (
	"fmt"
	"math/rand"
	"time"
)

// 生产者
func producer(header string, channel chan<- string) {
    
	for {
		// 将随机数和字符串格式化为字符串发送到通道
		channel <- fmt.Sprintf("%s: %v", header, rand.Int31())
        
		time.Sleep(time.Second)
	}
}

// 消费者
func consumer(channel <-chan string) {

	for {
		// 从通道中取出数据，此处会阻塞直到信道中返回数据
		message := <-channel
        
		fmt.Println(message)
	}
}

func main() {
	// 创建一个字符串类型的通道
	channel := make(chan string)
	// 创建producer函数的并发goroutine，即两个消费者
	go producer("cat", channel)
	go producer("dog", channel)
	// 数据消费函数
	consumer(channel)
}