package main
import (
    "fmt"
)

func main() {
    type baseUrlConfig struct {
        args []string
        url  string
    }
    baseUrlConfigs := []baseUrlConfig{}
    baseUrlConfigs = append(baseUrlConfigs, baseUrlConfig{[]string{"abctoken","aaa"}, "https://aaa.com/edf/send"})
    baseUrlConfigs = append(baseUrlConfigs, baseUrlConfig{[]string{"xyztoken","bbb"}, "https://bbb.com/abc/send"})
    
    for _,k := range baseUrlConfigs{
        //fmt.Println(i)
        fmt.Println(k.args)
        for _,arg := range k.args{
            fmt.Println(arg)
        }
        fmt.Println(k.url)
    }
}
