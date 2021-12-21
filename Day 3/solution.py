def to_binary(number):
    result = 0
    for idx, val in enumerate(reversed(number)):

        power = 2**idx
        if int(val) == 1:
            result += power
    return result





file_path = "C:/Users/aniak/Documents/Python - Advent Of Code/repo/Day 3/Input Data.txt"
f = open(file_path, "r").readlines()


# Part 1
gamma_rate = ""
epsilon_rate = ""

for x in range(0,12):
    count_x_1  = len([int(f[i][x]) for i in range(0,len(f)) if int(f[i][x]) == 1])
    count_x_0  = len([f[i] for i in range(0,len(f)) if int(f[i][x]) == 0])
    if count_x_1 > count_x_0:
        gamma_rate += "1"
        epsilon_rate  += "0"
    else:
        gamma_rate += "0"
        epsilon_rate  += "1"

result = to_binary(gamma_rate) * to_binary(epsilon_rate)
print(f'solution {result}')

# Part 2


temp_f = f

for x in range(0,12):
    count_x_1  = len([int(temp_f[i][x]) for i in range(0,len(temp_f)) if int(temp_f[i][x]) == 1])
    count_x_0  = len([temp_f[i] for i in range(0,len(temp_f)) if int(temp_f[i][x]) == 0])
    if count_x_1 >= count_x_0:
        temp_f = [(temp_f[i]) for i in range(0,len(temp_f)) if int(temp_f[i][x]) == 1]
    else:
        temp_f = [(temp_f[i]) for i in range(0,len(temp_f)) if int(temp_f[i][x]) == 0]

oxygen_generator_rating = to_binary(temp_f[0][:12])

temp_f = f
for x in range(0,12):
    if len(temp_f) > 1:
        count_x_1  = len([int(temp_f[i]) for i in range(0,len(temp_f)) if int(temp_f[i][x]) == 1])
        count_x_0  = len([temp_f[i] for i in range(0,len(temp_f)) if int(temp_f[i][x]) == 0])
        print(count_x_1)
    
        if count_x_1 < count_x_0:
            temp_f = [(temp_f[i]) for i in range(0,len(temp_f)) if int(temp_f[i][x]) == 1]
        else:
            temp_f = [(temp_f[i]) for i in range(0,len(temp_f)) if int(temp_f[i][x]) == 0]

print(temp_f)
c02_scrubber_rating = to_binary(temp_f[0][:12])
result = oxygen_generator_rating * c02_scrubber_rating
print(f'solution {result}')