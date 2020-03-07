package main

import "github.com/go-martini/martini"

func main() {
    m := martini.Classic()
    m.Get("/", func() string {
        return "Hello world!"
    })
    //m.Run()   //:3000
    m.RunOnAddr(":9000")
}
