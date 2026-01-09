package main

import (
    "context"
    "fmt"
    "time"

    "go.mongodb.org/mongo-driver/bson"
    "go.mongodb.org/mongo-driver/mongo"
    "go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
    defer cancel()

    client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://foo:bar@localhost:27017"))
    if err != nil {
        fmt.Println("连接失败:", err)
        return
    }
    defer client.Disconnect(ctx)

    // 查询样例 假设有表 my_user 存在以下字段
    type User struct {
        ID   string `bson:"_id,omitempty"`
        Name string `bson:"name"`
        Age  int    `bson:"age"`
    }
    collection := client.Database("test_db").Collection("my_user")
    cursor, err := collection.Find(ctx, bson.D{{Key: "name", Value: "admin"}})
    if err != nil {
        fmt.Println("查询失败:", err)
        return
    }
    for cursor.Next(ctx) {
        var user User
        if err := cursor.Decode(&user); err != nil {
            fmt.Println("解码失败:", err)
            continue
        }
        fmt.Printf("User: %+v\n", user)
    }

    fmt.Println(collection.Name())
    fmt.Println("连接成功")
}
