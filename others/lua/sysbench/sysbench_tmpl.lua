-- 用于sysbench
local t = sysbench.sql.type
-- local stmt_def = {
--       "SELECT c FROM sbtest1 WHERE id=?",
--       t.INT}
local stmt_def = { {{SQL_TMPL}} }

function thread_init(thread_id)
    drv = sysbench.sql.driver()
    con = drv:connect()
    
    stmt = {}
    param = {}
    
    stmt = con:prepare(string.format(stmt_def[1]))
    
    local nparam = #stmt_def - 1
    
    if nparam > 0 then
    param = {}
    end
    
    for p = 1, nparam do
    local btype = stmt_def[p+1]
    local len
    
    if type(btype) == "table" then
        len = btype[2]
        btype = btype[1]
    end
    if btype == sysbench.sql.type.VARCHAR or
        btype == sysbench.sql.type.CHAR then
            param[p] = stmt:bind_create(btype, len)
    else
        param[p] = stmt:bind_create(btype)
    end
    end
    
    if nparam > 0 then
    stmt:bind_param(unpack(param))
    end
end

local function get_id()
    return sysbench.rand.default(1, 1000)
end

local r = {}
local function get_string(r)
    local x = #r 
    return r[math.random(1,x)]
end

{{RAND_TABLE}}

function event(thread_id)
    {{PARAM_SET}}
    stmt:execute()
end


[[
替换的参数

SQL_TMPL
[[SELECT c FROM sbtest1 WHERE id=? and c=?]], t.INT, {t.CHAR, 120}
 

RAND_TABLE 
local a = {"aaa","bbbb","ccc"} 
 

PARAM_SET      
param[1]:set(get_id())
param[2]:set(get_string(a))  
            
            
]]
