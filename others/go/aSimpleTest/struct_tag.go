package main

import (
    "fmt"
    "encoding/json"
)


type address struct {
    Street  string `json:"street"`              // 设置别名
    Ste     string `json:"suite,omitempty"`     // 使用omitempty标记不存在时省略
    City    string `json:"city"`                // 
    State   string `json:"state"`               // 
    Zipcode string `json:"zipcode"`             // 
}

func main() {
    data := `{
        "street": "200 Larkin St",
        "city": "San Francisco",
        "state": "CA",
        "zipcode": "94102"
    }`
    addr := new(address)
    json.Unmarshal([]byte(data), &addr)
    
    addressBytes, _ := json.MarshalIndent(addr, "", "    ")
    fmt.Printf("%s\n", string(addressBytes))
}