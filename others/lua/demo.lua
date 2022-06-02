
-- for t = 1, 10 do
--     -- print(t)
--     stmt_defs = {
--       "SELECT c FROM sbtest%u WHERE id=?","aaa"}
--     print(string.format(stmt_defs[1],1))
--     
--     
-- end
-- 
-- local stmt_def = {
--       "SELECT c FROM sbtest%u WHERE id=?",
--       "aaa","bbb"}
--       
-- local nparam = #stmt_def - 1
-- 
-- print(nparam)


local a= {"aaa","bbb","ccc"}


local x = #a

for t = 1, 10 do
-- local k = sysbench.rand.default(1, x)
local k = math.random(1,x)
print(a[k])
end

