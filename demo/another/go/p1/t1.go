package io

type Writer interface {
    Write(p []byte) (n int, err error)
}
type Closer interface {
    Close() error
}
type WriteCloser interface {
    Writer
    Closer
}
