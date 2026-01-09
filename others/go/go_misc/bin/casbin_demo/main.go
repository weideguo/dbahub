package main

// 访问控制框架

import (
    "fmt"
    "log"

    "github.com/casbin/casbin/v2"
)

func check(e *casbin.Enforcer, sub, obj, act string) {
    ok, _ := e.Enforce(sub, obj, act)
    if ok {
        fmt.Printf("%s CAN %s %s\n", sub, act, obj)
    } else {
        fmt.Printf("%s CANNOT %s %s\n", sub, act, obj)
    }
}

func main() {
    e, err := casbin.NewEnforcer("./model.conf", "./policy.csv")
    if err != nil {
        log.Fatalf("NewEnforecer failed:%v\n", err)
    }

    check(e, "user1", "data1", "read")
    check(e, "user1", "data1", "write")
    check(e, "user1", "data2", "read")
    check(e, "user1", "data2", "write")

    check(e, "user2", "data1", "read")
    check(e, "user2", "data1", "write")
    check(e, "user2", "data2", "read")
    check(e, "user2", "data2", "write")

    check(e, "root", "data2", "write")
}
