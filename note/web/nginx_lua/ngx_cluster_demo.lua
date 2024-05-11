-- 需要预先安装
-- https://github.com/steve0511/resty-redis-cluster
local redis_cluster = require "rediscluster"

local config = {
    name = "rediscluster", 
    serv_list = {
        {ip="192.168.201.128", port = 7001},
        {ip="192.168.201.128", port = 7002},
        {ip="192.168.201.128", port = 7003},
        {ip="192.168.201.128", port = 7004},
        {ip="192.168.201.128", port = 7005},
        {ip="192.168.201.128", port = 7006}
    },
    keepalive_timeout = 60000,
    keepalive_cons = 1000,
    connection_timeout = 10,
    max_redirection = 5,
    max_connection_attempts = 1,
    auth = "foobared"
}

--
local client = redis_cluster:new(config)
