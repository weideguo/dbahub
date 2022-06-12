package main

import (
	"flag"
	"fmt"
    "os"
    
    "github.com/gugemichael/nimo4go"
    
    "configParserDemo/config"
)

func main() {
    var err error
    configuration := flag.String("conf", "./demo.conf", "configuration path")
    flag.Parse()
    fmt.Println(*configuration)
    
    var file *os.File
    if file, err = os.Open(*configuration); err != nil {
        panic(fmt.Sprintf("Configure file open failed. %v", err))
    }

    configure := nimo.NewConfigLoader(file)
    
    if err := configure.Load(&config.Options); err != nil {
		panic(fmt.Sprintf("Configure file %s parse failed. %v", *configuration, err))
	}
    
    fmt.Println(config.Options.Id       ) 
    fmt.Println(config.Options.LogFile  ) 
    fmt.Println(config.Options.LogLevel ) 
    fmt.Println(config.TypeSync         ) 
    
  
}