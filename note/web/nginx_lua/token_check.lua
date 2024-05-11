-- 进行token验证，可以在header或者get的请求参数
local pool_size = 3
local pool_max_idle_time = 1000
local redis_connection_timeout = 100
local redis_host = "127.0.0.1"
local redis_port = 6379
local redis_auth = "my_redis_passwd";


local function errlog(msg, ex)
    ngx.log(ngx.ERR, msg, ex)
end

-- redis
local function close_redis(client)
    if not client then
        return
    end
    local ok, err = client:set_keepalive(pool_max_idle_time, pool_size)
    if not ok then
        ngx.say("redis connct err:",err)
        return client:close()
    end
end

local redis = require "resty.redis"
local client = redis:new()
local ok, err = client:connect(redis_host, redis_port)

if not ok then
    close_redis(client)
    ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
end

client:set_timeout(redis_connection_timeout)


local connCount, err = client:get_reused_times()
if  0 == connCount then
    local ok, err = client:auth(redis_auth)
    if not ok then
        errlog("failed to auth: ", err)
        return
    end
elseif err then
    errlog("failed to get reused times: ", err)
    return
end

-- token
local function getToken()
    local token = ngx.req.get_headers()["token"]
    if token == nil then
        -- ngx.req.get_body_data
        token = ngx.req.get_uri_args()["token"]
        if token == nil then
            ngx.say("get token from header and uri args is nil, error:",err)
            ngx.exit(ngx.HTTP_FORBIDDEN)
        end
    end
    return token
end

local reqToken = getToken();


local tokenInfo,err = client:get(reqToken)
-- say和exit只能用一个
if err then
--ngx.say("redis get token error:",err)
ngx.exit(ngx.HTTP_FORBIDDEN)
end

if not tokenInfo then
-- ngx.say("redis get token not exist")
ngx.exit(ngx.HTTP_FORBIDDEN)
elseif tokenInfo == nil then
-- ngx.say("redis get token is nil")
ngx.exit(ngx.HTTP_FORBIDDEN)
elseif tokenInfo == "" then
-- ngx.say("redis get token empty", tokenInfo)
ngx.exit(ngx.HTTP_FORBIDDEN)
elseif tokenInfo== ngx.null then
ngx.status = 201
ngx.header["Content-Type"] = "application/json"
ngx.say("{\"msg\":\"redis get token is null\"}")
-- ngx.say("redis get token is null")
ngx.exit(ngx.HTTP_FORBIDDEN)
else
-- ngx.say("redis get token:", string.len(tokenInfo))
end

close_redis(client)

