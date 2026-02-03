package plugin

import "fmt"

type m2 struct {
}

func (m *m2) Setup() {
    fmt.Printf("m2 Setup\n")
}

func (m *m2) Fetch(location string) {
    fmt.Printf("m2 Fetch %s\n", location)
}

func init() {
    AllBackends["m2"] = &m2{}
}
