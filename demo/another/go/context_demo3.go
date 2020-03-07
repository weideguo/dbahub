package main
import (
    "context"
    "fmt"
)
func main() {
    f := func(ctx context.Context, k string) {
        if v := ctx.Value(k); v != nil {
            fmt.Println("found: ", v, k)
        } else{
            fmt.Println("not found: ", k)
        }
    }
    k := "aaaa"
    v := "vvvv123"
    ctx := context.WithValue(context.Background(), k, v)
    f(ctx, k)
    f(ctx, "colorxxx")
}
