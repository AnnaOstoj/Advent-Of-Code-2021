#Part 1

file_path = "C:/Users/aniak/Documents/Python - Advent Of Code/Day 1/Input Data.txt"
f = open(file_path, "r").readlines()

x_0 = int(f[0])
count = 0


for x in f:
    x = int(x)
    if x > x_0:
        count += 1
    x_0 = x
print(count)

#Part 2
count = 0

for i in range(0,(len(f)-3)):
    sum_1 = (int(f[i]) + int(f[i+1]) + int(f[i+2]))
    sum_2 = (int(f[i+1]) + int(f[i+2]) + int(f[i+3]))

    if sum_1 < sum_2:
        count += 1
print(count)
