Sum_Even = 0

for i = 1, 100 do
    if (i % 2 == 0) then
        Sum_Even = Sum_Even + i
    end
end

print("The Sum of even numbers from 0 - 100 is "..Sum_Even)