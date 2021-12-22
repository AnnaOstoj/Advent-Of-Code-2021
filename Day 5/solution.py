
import pandas as pd
import numpy as np


def get_item(item):
    
    if "\n" in item and len(item) > 1:
        list_temp = [item[:item.find(' -> ')], item[item.find(' -> ') + 4:item.find('\n')]]
        return ','.join([str(item) for item in list_temp])
    elif len(item) > 1:
        list_temp = [item[:item.find(' -> ')],item[item.find(' -> ') + 4:]]
        return ','.join([str(item) for item in list_temp])


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
board = np.zeros((int(board_size)+2,int(board_size)+2))

#find dangerous places

for index, row in data.iterrows():
    if index < int(board_size) + 1:
        if row["x1"] == row["x2"]: # vertical movement
            # count steps
            vertical_steps = row["y2"] - row["y1"]
            if vertical_steps > 0:  #move down

                for i in range(row["y1"], row["y2"] + 1):
                    board[i,row["x1"]] += 1
            else: # move up

                for i in range(row["y2"],row["y1"] + 1):
                    board[i,row["x1"]] += 1

        if row["y1"] == row["y2"]: # horizontal movement
            # count steps
            horizontal_steps = row["x2"] - row["x1"]
            if horizontal_steps > 0: # move right
                for i in range(row["x1"] , row["x2"] + 1):
                    board[row["y1"], i] += 1
            else: #move left
                for i in range(row["x2"] , row["x1"] + 1):
                    board[row["y1"], i] += 1

#count dangerous places
dangerous_places = np.count_nonzero(board[:] >= 2)
print(f' Dangerous places: {dangerous_places}')