package main
import (
    "fmt"
    "log"
    "net/http"
    "io/ioutil"
)

func sayHello(w http.ResponseWriter, r *http.Request) {
    log.Println(r)
    b,_ := ioutil.ReadAll(r.Body)
    log.Println(string(b))
    fmt.Fprintf(w, "request success")
}

func main() {
    http.HandleFunc("/", sayHello)
    log.Println("listen on localhost:9000")
    err := http.ListenAndServe(":9000", nil)
    if err != nil {
        log.Fatal("List 9000")
    }
}
