package main

import (
    "crypto/tls"
    "fmt"
    "net/http"
)

func main() {

    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{InsecureSkipVerify: true}, // 忽略服务器SSL证书的验证
        },
    }

    resp, err := client.Get("https://www.baidu.com")
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    for _, cert := range resp.TLS.PeerCertificates {
        fmt.Printf("-------------------------------------\n")
        fmt.Printf("Certificate details:\n")
        fmt.Printf("DNSNames: %v\n", cert.DNSNames)
        fmt.Printf("Not valid before: %v\n", cert.NotBefore)
        fmt.Printf("Not valid after: %v\n", cert.NotAfter)
        fmt.Printf("Is CA: %t\n", cert.IsCA)
        fmt.Printf("Subject: %v\n", cert.Subject)
        fmt.Printf("Issuer: %v\n", cert.Issuer)
        fmt.Printf("Signature algorithm: %v\n", cert.SignatureAlgorithm)
        //cert.
    }
}
