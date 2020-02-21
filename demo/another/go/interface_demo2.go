package main
import "fmt"


// 一个服务需要满足能够开启和写日志的功能
type Service interface {
    Start()  // 开启服务
    Log(string)  // 日志输出
}

// 日志器
type Logger struct {
}
// 实现Service的Log()方法
func (g *Logger) Log(l string) {
    fmt.Println(l)
}

// 游戏服务
type GameService struct {
    Logger  // 嵌入日志器
}
// 实现Service的Start()方法
func (g *GameService) Start() {
    fmt.Println("service start")
}


func f1(){
    // var s GameService = &GameService{}  //这种使用方式有错误
    var s Service = new(GameService)
    //var s Service 
    //s = new(GameService)
    
    s.Start()
    s.Log("output log")
}

func f2(){
    
    //以下三种都可以 
    //var s GameService
    s := &GameService{}
    //s := new(GameService)

    s.Start()
    s.Log("output log")
}


func main(){
    // 使用接口
    //f1()
    
    // 不使用接口
    f2()

}

