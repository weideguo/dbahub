package main

// 用支持自定义url的执行，通过修改windows的注册表，实现在浏览器中通过自定义url执行对应二进制文件
// 该程序可以接收浏览器传递的参数，进行转换，然后传给指定的可执行的文件，以实现自定义url对应自定义功能

import (
        "flag"
        "fmt"
        "regexp"
        "strings"
        "os/exec"
    )

var exe = flag.String("exe", "", "可执行的文件")    
var surl = flag.String("surl", "", "自定义的url，格式如：`wdg://www.sysu.edu.cn`，将只传`www.sysu.edu.cn`给可执行文件")    
    
func main() {
    flag.Parse()

    // cmd := exec.Command("C:\\Program Files\\Internet Explorer\\iexplore.exe", "www.sysu.edu.cn")
    // re := regexp.MustCompile(`(?<=(\://)).*`)   // 不支持lookaround
    re := regexp.MustCompile(`.+?://.+`)   
    _url := re.FindString(*surl)
    if _url == "" {
        panic("surl must like: `wdg://www.sysu.edu.cn`")
    }
    _surl := strings.Split(*surl, "://")
    if len(_surl) != 2 {
        panic("surl should not include too mush: `://`")
    }
    
    url := _surl[1]
    
    fmt.Println(*exe, url)
    
    cmd := exec.Command(*exe, url)
    out, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Printf("failed %s\n", err)
	}
	fmt.Printf("output %s\n", string(out))
    fmt.Printf("done\n")
}



