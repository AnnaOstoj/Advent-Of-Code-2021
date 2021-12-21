import numpy as np
from numpy.core.defchararray import isnumeric
import pandas as pd

numbers = [6,69,28,50,36,84,49,13,48,90,1,33,71,0,94,59,53,58,60,96,30,
            34,29,91,11,41,77,95,17,80,85,93,7,9,74,89,18,25,26,8,87,38,
            68,5,12,43,27,46,62,73,16,55,22,4,65,76,54,52,83,10,21,67,15,47,
            45,40,35,66,79,51,75,39,64,24,37,72,3,44,82,32,78,63,57,2,86,31,
            19,92,14,97,20,56,88,81,70,61,42,99,23,98]

file_path = "C:/Users/aniak/Documents/Python - Advent Of Code/repo/Day 4/Input Data.txt"
f = open(file_path, "r").readlines()
data = pd.DataFrame(f)

def get_item(item):
    
    if "\n" in item and len(item) > 1:
        return item[:item.find('\n')]
    elif len(item) > 1:
        return item

def to_numbers(item):
    numbers = item.split(' ')
    row = []
    for el in numbers:
        if isnumeric(el):
            row.append(int(el))
    return row

def check_number(board, num):
    for id, row in enumerate(board):
        for idx, el in enumerate(row):
            if el == num:
                board[id][idx] = 'T'
    return board

def check_horizontal_bingo(board):
    if board.count("T") == 5:
        return True
    else:
        return False

def check_vertical_bingo(board):
    found = False
    for i in range(0,len(board[0])):
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] and board[0][i] == "T":
            
            found = True
    return found


def sum_int_elements(board):
    sum_of_unmarked = 0
    for line in board:
        for el in line:
            if el != "T":
                sum_of_unmarked += int(el)
    return sum_of_unmarked

cleaned_data = data.applymap(get_item)
cleaned_data = cleaned_data.dropna()

cleaned_data = cleaned_data.applymap(to_numbers)
cleaned_data = cleaned_data[0].tolist()

boards = []
for i in range(0,len(cleaned_data)-4, 5):
    boards.append(cleaned_data[i:i+5])

game_boards = boards

for num in numbers:

    result = 0
    for id, board in enumerate(game_boards):

        board = check_number(board, num)


        game_boards[id] = board
        #check if bingo
        if check_horizontal_bingo(board) or check_vertical_bingo(board):
            print(f'We have a winner with id = {id} for num: {num}')

            
            sum_of_elements = sum_int_elements(board)
            result = num * sum_of_elements
            print(f'sum of elements: {sum_of_elements}')
            print(f'result: {result}')


    if result != 0:
        break



