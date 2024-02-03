package main

import (
	"fmt"
	"encoding/json"
)


func main() {
//b := []byte(`{"appCode":"CMW","resStatus":504,"resMsg":"\u57df\u540d\u670d\u540d\u670d\u52a1\u7c7b\u578b\u6709\u8bef\uff01","data":null}`)

b1 := `"\u57df\u540d"`
//b1 := "\\u57df\\u540d"
b:=[]byte(fmt.Sprintf(`{"x":%s}`,b1))

//fmt.Println(string(b))
m := make(map[string]interface{})
json.Unmarshal(b,&m)
j,_ := json.Marshal(m)

fmt.Println(string(j))
}