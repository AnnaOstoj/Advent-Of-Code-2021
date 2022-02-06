from contextlib import closing
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from common import get_input
 
brackets = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<"
}
closing_brackets_scoring = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

counter =  {
    ")" : 0,
    "]" : 0,
    "}" : 0,
    ">" : 0
}


def find_not_matching_bracket(row):
    for i in range(1,len(row)):
        if row[i] in brackets.keys():
            if brackets[row[i]] != row[i-1]:
                counter[row[i]] += 1
                break
            else:
                row = row[0 : i-1 : ] + row[i + 1 : :]
                return find_not_matching_bracket(row)


input_data = get_input.get_input_data()

for row in input_data:
    find_not_matching_bracket(row)

result = counter[")"] * closing_brackets_scoring[")"] + \
         counter["]"] * closing_brackets_scoring["]"] + \
         counter["}"] * closing_brackets_scoring["}"] + \
         counter[">"] * closing_brackets_scoring[">"] 

print(result)

