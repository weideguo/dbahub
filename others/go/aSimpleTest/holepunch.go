package main

import (
    "log"
    "os"
    "syscall"
)

//  mode 0 change to size                  0x0
//  FALLOC_FL_KEEP_SIZE                  = 0x1
//  FALLOC_FL_PUNCH_HOLE                 = 0x2
func punchHoleLinux(file *os.File, offset int64, size int64) error {
    return syscall.Fallocate(int(file.Fd()), 0x1|0x2, offset, size)
}

// dd if=/dev/urandom of=./test.txt.4M bs=1M count=4  
// 打洞之后表现为
// du -s test.txt.4M      #显示为4m
// ls -altr test.txt.4M   #显示为2m
// 打洞之后0-2M的部分读出来全部为0
//
// 利用：mysql页透明压缩技术，使用压缩算法对每个page进行压缩，然后进行打洞，从而实现磁盘空间释放

func main() {
    f, err := os.OpenFile("./test.txt.4M", os.O_RDWR|os.O_CREATE, 0666)
    if err != nil {
        log.Fatalf("open failed. err(%v)\n", err)
    }

    // 打洞的开始偏移量
    // 打洞的大小
    // 打洞之后这个位置读出来的数据都为0，表现为一个虚假的空间占用（空间被回收给操作系统，但可以读这部分空间）
    err = punchHoleLinux(f, 0, 2*1024*1024)
    if err != nil {
        log.Fatalf("punch hole failed")
    }

    log.Printf("punch hole success.\n")
}