package main

import (
    "fmt"
    "encoding/json"
    "gopkg.in/mgo.v2"
    "gopkg.in/mgo.v2/bson"
)

func main() {
    mongodb_uri := "mongodb://dba:dba@127.0.0.1:27017/admin"     //strings $filename  #编译后还是可以看到明文信息
    session, err := mgo.Dial(mongodb_uri)
    if err != nil {
        panic(err)
    }
    defer session.Close()

    // Optional. Switch the session to a monotonic behavior.
    session.SetMode(mgo.Monotonic, true)
    result := bson.M{}
    if err := session.DB("admin").Run(bson.D{{"serverStatus", 1}}, &result); err != nil {
        panic(err)
    } else {
        //fmt.Println(result)
        jsonStr, err := json.Marshal(result)
           if err != nil {
                panic(err)
        }
        fmt.Println(string(jsonStr))

    }

}