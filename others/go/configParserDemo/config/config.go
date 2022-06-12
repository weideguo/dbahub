package config

type Configuration struct {
	Id                     string   `config:"id"`
	LogFile                string   `config:"log.file"`
	LogLevel               string   `config:"log.level"`

}

var Options Configuration

const (
	TypeSync    = "sync"
)

