import os
import sys
import pandas as pd

def get_item(item):
    
    if "\n" in item and len(item) > 1:
        return item[:item.find('\n')]
    elif len(item) > 1:
        return item

def get_locations_list(row_index, column_index, data):
    current = data[row_index][column_index]
    left = data[row_index][column_index - 1] if column_index > 0 else None
    right = data[row_index][column_index + 1] if column_index < 99 else None
    down = data[row_index + 1][column_index] if row_index < 99 else None
    up = data[row_index - 1][column_index] if row_index > 0 else None
    # remve None values and convert to number
    return [int(i) for i in [current, left, right, down, up] if i] 

f = open(os.path.join(sys.path[0], 'Input Data.txt')).readlines()

data = pd.DataFrame(f)
data = data.applymap(get_item)

lowest_points = []
for row_index in range(0, len(data[0])):
    for column_index in range(0, len(data[0])):
        current_loc = int(data[0][row_index][column_index])
        locations_list = get_locations_list(row_index, column_index, data[0])
        min_value = min(locations_list)
        if current_loc == min_value and \
            locations_list.count(current_loc) < 2  :
            lowest_points.append(current_loc)

result = sum([int(i) + 1 for i in lowest_points])
print(f'Part One: {result}')
        

