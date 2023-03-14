function thread_init(thread_id)

-- set_vars()

db_connect()

end

function event(thread_id)

local table_name

local rs

table_name = "sbtest1"

-- db_query("begin")

for i=1, 10000 do

rs = db_query("SELECT * FROM ".. table_name .." WHERE id=" .. i)

end

end