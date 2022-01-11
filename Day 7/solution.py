import os
import sys

f = open(os.path.join(sys.path[0], 'Input Data.txt')).read()
data = f.split(',')
data = list(map(lambda x: int(x), data))
max_value = max(data)

# Part One
fuel_list = []

for x in range(1, max_value + 1): 
    list_of_fuel = [abs(x - i) for i in data]
    fuel_sum = sum(list_of_fuel)
    fuel_list.append(fuel_sum)

min_fuel_cost = min(fuel_list)
print(f'Part One: {min_fuel_cost}')

# Part Two

def calculate_fuel(i, x):
    n = abs(x - i)
    a1 = 1
    an = abs(x - i)
    fuel = (a1 + an)/2*n
    return fuel

fuel_list = []

for x in range(1, max_value + 1): 
    list_of_fuel = [calculate_fuel(i, x) for i in data]
    fuel_sum = sum(list_of_fuel)
    fuel_list.append(fuel_sum)

min_fuel_cost = min(fuel_list)
print(f'Part Two: {min_fuel_cost}')

