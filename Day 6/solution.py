import pandas as pd

file_path = "C:/Users/aniak/Documents/Python - Advent Of Code/repo/Day 6/Input Data.txt"
f = open(file_path, "r").read()

# prepare data
f = f.split(',')
data = [int(x) for x in f]
data = pd.DataFrame(data)
print(f'Original number of lanternfish is equal to: {len(data)}')

change_dict = {0:6, 
        1:0,
        2:1,
        3:2,
        4:3,
        5:4,
        6:5,
        7:6,
        8:7
        }

def make_an_update(x):
    x = change_dict[x]
    return x

for i in range(0,80):

    number_newborns = data[0].tolist().count(0)
    data = data.applymap(make_an_update)
    list_of_newborns = pd.DataFrame([8 for i in range(0,number_newborns)])
    data = data.append(list_of_newborns)

print(f'Number of lanternfish after 80 days is equal to: {len(data)}')

