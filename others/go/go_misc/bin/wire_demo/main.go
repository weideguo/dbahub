package main

import (
    "errors"
    "fmt"
    "os"
    "time"
)

type Message string

func NewMessage(phrase string) Message {
    return Message(phrase)
}

func NewGreeter(m Message) Greeter {
    var grumpy bool
    if time.Now().Unix()%2 == 0 {
        grumpy = true
    }
    return Greeter{Message: m, Grumpy: grumpy}
}

type Greeter struct {
    Grumpy  bool
    Message Message
}

// Greet produces a greeting for guests.
func (g Greeter) Greet() Message {
    if g.Grumpy {
        return Message("Go away!")
    }
    return g.Message
}

// NewEvent creates an event with the specified greeter.
func NewEvent(g Greeter) (Event, error) {
    if g.Grumpy {
        return Event{}, errors.New("could not create event: event greeter is grumpy")
    }
    return Event{Greeter: g}, nil
}

// Event is a gathering with greeters.
type Event struct {
    Greeter Greeter
}

// Start ensures the event starts with greeting all guests.
func (e Event) Start() {
    msg := e.Greeter.Greet()
    fmt.Println(msg)
}

func main() {
    e, err := InitializeEvent("hi there!")
    if err != nil {
        fmt.Printf("failed to create event: %s\n", err)
        os.Exit(2)
    }
    e.Start()
}
