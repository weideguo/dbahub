package main

import (
    "bytes"
    "encoding/json"
    // "io"
    "io/ioutil"
    "net/http"
    "time"
    "fmt"
)

// GET
// url：         请求地址
// response：    请求返回的内容
func Get(url string) string {

    client := &http.Client{Timeout: 5 * time.Second}
    resp, err := client.Get(url)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()
    
    // var buffer [512]byte                          // 返回大量数据时的处理
    // result := bytes.NewBuffer(nil)
    // for {
    //     n, err := resp.Body.Read(buffer[0:])
    //     result.Write(buffer[0:n])
    //     if err != nil && err == io.EOF {
    //         break
    //     } else if err != nil {
    //         panic(err)
    //     }
    // }
    // return result.String()

    result, _ := ioutil.ReadAll(resp.Body)
    return string(result)
}

// POST
// url：         请求地址
// data：        POST请求提交的数据
// contentType： 请求体格式，如：application/json
// content：     请求放回的内容
func Post(url string, data interface{}, contentType string) string {

    client := &http.Client{Timeout: 5 * time.Second}
    jsonStr, _ := json.Marshal(data)
    resp, err := client.Post(url, contentType, bytes.NewBuffer(jsonStr))
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    result, _ := ioutil.ReadAll(resp.Body)
    return string(result)
}

func main() {
    r := Get("http://www.baidu.com")
    fmt.Println(r)
    
    // data := map[string]string{
    //     "username":"admin",
    //     "password":"weideguo"}
    // 
    // r := Post("http://127.0.0.1:8000/api/v1/login/", data, "application/json")
    // fmt.Println(r)
}

