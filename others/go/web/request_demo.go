package main
import (
    "bytes"
    "flag"
    "fmt"
    "log"
    "net/http"
    // "mime/multipart"
)



func getRequestBody( params map[string]string) (*bytes.Buffer) {
    body := &bytes.Buffer{}
    // writer := multipart.NewWriter(body)    // 上传文件 mime/multipart内容
    // for key, val := range params {
    //     _ = writer.WriteField(key, val)
    // }
    // writer.Close()
    return body
}
func main() {
    flag.Parse()
    url := flag.Arg(0)   // url 命令行参数引入访问的url

    extraParams := map[string]string{
        // "Test": "",
    }
    body := getRequestBody(extraParams)
    request, err := http.NewRequest("GET", url, body)
    
    if err != nil {
        log.Fatal(err)
    }
    request.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
    request.Header.Set("Content-Type", "text/html; charset=utf-8")
    request.Header.Set("Accept", "application/json; charset=utf-8")
    // request.Header.Set("Content-Type", "application/json; charset=utf-8")
    // request.Header.Set("Accept", "text/html; charset=utf-8")
    client := &http.Client{}
    resp, err := client.Do(request)
    if err != nil {
        log.Fatal(err)
    } else {
        /* 读取response返回数据 */
        body := &bytes.Buffer{}
        _, err := body.ReadFrom(resp.Body)
        if err != nil {
            log.Fatal(err)
        }
        resp.Body.Close()
        fmt.Println(resp.StatusCode)
        fmt.Println(resp.Header)
        fmt.Println(body)
    }
}

    
    