Numbers = {
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
}

for i = 10, 1, -1 do
    for k, v in ipairs(Numbers) do
        print(v, "\n")
    end
    table.remove(Numbers, i)
end