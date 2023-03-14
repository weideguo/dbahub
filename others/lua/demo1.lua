
local stmt_def = { [[select * from a ]], 111 }

local nparam = #stmt_def - 1
print(nparam)

for p = 1, 1 do
    print(p)
end
