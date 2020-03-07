package my_test

import "testing"

func Benchmark_Add_TimerControl(b *testing.B) {
    // 重置计时器
    b.ResetTimer()
    // 停止计时器
    b.StopTimer()
    // 开始计时器
    b.StartTimer()
    var n int
    for i := 0; i < b.N; i++ {
        n++
    }
}

/*
通过控制计时器，让计时器只在需要的区间进行测试。
*/
