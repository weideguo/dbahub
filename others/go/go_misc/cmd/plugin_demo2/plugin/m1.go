package plugin

import "fmt"

type m1 struct {
}

func (m *m1) Setup() {
    fmt.Printf("m1 Setup\n")
}

func (m *m1) Fetch(location string) {
    fmt.Printf("m1 Fetch %s\n", location)
}

func init() {
    AllBackends["m1"] = &m1{}
}
