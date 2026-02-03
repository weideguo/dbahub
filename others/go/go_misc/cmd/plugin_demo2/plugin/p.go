package plugin

type Backend interface {
    Setup()
    Fetch(location string)
}

var (
    AllBackends = make(map[string]Backend)
)
