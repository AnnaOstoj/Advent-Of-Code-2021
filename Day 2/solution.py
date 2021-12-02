file_path = "C:/Users/aniak/Documents/Python - Advent Of Code/Day 2/Input Data.txt"
f = open(file_path, "r").readlines()

# Part 1

horizontal = 0
depth = 0

for x in f:
    x = x.strip()
    if x.startswith('down'):
        depth += int(x[-1])
    if x.startswith('up'):
        depth -= int(x[-1])
    if x.startswith('forward'):
        horizontal += int(x[-1])

result = horizontal * depth
print(f'depth {depth}, horizontal {horizontal}')
print(f'multiply {result}')

# Part 2

horizontal = 0
depth = 0
aim = 0

for x in f:
    x = x.strip()
    if x.startswith('down'):
        aim += int(x[-1])
    if x.startswith('up'):
        aim -= int(x[-1])
    if x.startswith('forward'):
        horizontal += int(x[-1])
        depth += aim*int(x[-1])

result = horizontal * depth
print(f'depth {depth}, horizontal {horizontal}')
print(f'multiply {result}')