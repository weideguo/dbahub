package main

// 访问控制框架 ABAC（attribute base access list）

import (
    "fmt"
    "log"

    "github.com/casbin/casbin/v2"
)

type Object struct {
    Name  string
    Owner string
}

type Subject struct {
    Name string
    Hour int
}

func check(e *casbin.Enforcer, sub Subject, obj Object, act string) {
    ok, _ := e.Enforce(sub, obj, act)
    if ok {
        fmt.Printf("%s CAN %s %s at %d:00\n", sub.Name, act, obj.Name, sub.Hour)
    } else {
        fmt.Printf("%s CANNOT %s %s at %d:00\n", sub.Name, act, obj.Name, sub.Hour)
    }
}

func main() {
    e, err := casbin.NewEnforcer("./model.conf", "./policy.csv")
    if err != nil {
        log.Fatalf("NewEnforecer failed:%v\n", err)
    }

    o := Object{"data", "user1"}
    s1 := Subject{"user1", 10}
    s2 := Subject{"user1", 20}

    s3 := Subject{"user2", 10}
    s4 := Subject{"user2", 20}

    check(e, s1, o, "read")
    check(e, s2, o, "read")
    check(e, s3, o, "read")
    check(e, s4, o, "read")
}
