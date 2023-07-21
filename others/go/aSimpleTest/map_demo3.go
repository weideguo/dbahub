package main

import "fmt"

func main() {
    results := make(map[string][]interface{})
    results["a"] =append(results["a"],1111)
    results["a"] =append(results["a"],2222)
    results["b"] =append(results["b"],111111)
    results["b"] =append(results["b"],222222)
    //results["b"] = 1
    //results["b"] = results["b"]+1
    for k, v := range results {
        fmt.Println(k)
        var x int
        for _,vv := range v{
            //fmt.Println(vv)
            vvv,_ := vv.(int)
            x += vvv
        }
        fmt.Println(x)
    }
    //fmt.Println(results)
}
