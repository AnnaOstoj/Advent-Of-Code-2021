
import pandas as pd
import numpy as np


def get_item(item):
    
    if "\n" in item and len(item) > 1:
        list_temp = [item[:item.find(' -> ')], item[item.find(' -> ') + 4:item.find('\n')]]
        return ','.join([str(item) for item in list_temp])
    elif len(item) > 1:
        list_temp = [item[:item.find(' -> ')],item[item.find(' -> ') + 4:]]
        return ','.join([str(item) for item in list_temp])

def get_movement_type(a,b):
    # 0 if no movement
    # 1 if to right or down
    # -1 if to left or down
    if a == b:
        return 0
    elif a < b:
        return 1
    else:
        return -1

# get and clean data to get coordinates in separate columns

file_path = "C:/Users/aniak/Documents/Python - Advent Of Code/repo/Day 5/Input Data.txt"
f = open(file_path, "r").readlines()
data = pd.DataFrame(f)
data = data.applymap(get_item)

data[["x1", "y1", "x2", "y2"]] = data[0].str.split(",", expand=True)
data = data.drop(data.columns[[0]], axis = 1)
data = data.apply(pd.to_numeric)

#create board of zero values with size of the maximum coordinates and small margin
max_x1 = data["x1"].max()
max_x2 = data["x2"].max()
max_y1 = data["x1"].max()
max_y2 = data["x1"].max()
board_size = max(max_x1, max_x2, max_y1, max_y2)
board = np.zeros((int(board_size) + 2, int(board_size) + 2))

#find dangerous places

for index, row in data.iterrows():

    if index < int(board_size) + 1:

        distance = max(abs(row["x2"] - row["x1"]), abs(row["y2"] - row["y1"])) 
        
        for i in range(distance + 1):
            movement_y = get_movement_type(row["y1"],row["y2"])
            movement_x = get_movement_type(row["x1"],row["x2"])
            board[row["x1"] + i * movement_x, row["y1"] + i * movement_y] += 1

#count dangerous places
dangerous_places = np.count_nonzero(board[:] >= 2)
print(f' Dangerous places: {dangerous_places}')