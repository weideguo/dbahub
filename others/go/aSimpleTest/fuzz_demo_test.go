package main

import (
	"testing"
	"unicode/utf8"
)

func FuzzReverse(f *testing.F) {
	// 多个测试样例
	testcases := []string{"Hello, world", "how", "are", "you"}
	for _, tc := range testcases {
		f.Add(tc)
	}
	// Fuzz 1.8 引入，用于覆盖更多的测试样例
	f.Fuzz(func(t *testing.T, orig string) {

		rev, err1 := Reverse(orig)
		if err1 != nil {
			return
		}
		doubleRev, err2 := Reverse(rev)
		if err2 != nil {
			return
		}
		if orig != doubleRev {
			t.Errorf("Before: %q, after: %q", orig, doubleRev)
		}
		if utf8.ValidString(orig) && !utf8.ValidString(rev) {
			t.Errorf("Reverse produced invalid UTF-8 string %q", rev)
		}
	})
}
