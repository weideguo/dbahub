// 加载json文件，并反系列化
fetch("url_for_json_file.json").then((res) => res.json()).then((res) => {
    data = res;
})


