var fs = require("fs")
var http = require("http");

var server = http.createServer()

server.on("request",function (req, res) {
  var fileName = "." + req.url;

  if (fileName === "./stream") {
    res.writeHead(200, {
      "Content-Type":"text/event-stream",
      "Cache-Control":"no-cache",
      "Connection":"keep-alive",
      "Access-Control-Allow-Origin": "*",
    });
    res.write("retry: 10000\n");
    res.write("event: connecttime\n");
    res.write("data: " + (new Date()) + "\n\n");
    res.write("data: " + (new Date()) + "\n\n");

    interval = setInterval(function () {
      res.write("data: " + (new Date()) + "\n\n");
    }, 1000);

    req.connection.addListener("close", function () {
      clearInterval(interval);
    }, false);
  } else {
    var data = fs.readFileSync("./client.html", "utf8")
    res.write(data)
    res.end()
  }
    
})

server.listen(8844, "0.0.0.0");
/*
 * Server-sent Events
 * 通过长连接实现服务端推送数据给客户端 WebSocket 的一种轻量代替方案
 *
 * node server.js
 *
 * */
