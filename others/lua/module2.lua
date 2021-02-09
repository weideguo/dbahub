
-- 根据不同的lua启动位置，需要修改require的路径
xx=require("module")

moduley = {}

moduley.x = xx

return moduley

