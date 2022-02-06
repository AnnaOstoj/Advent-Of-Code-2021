from contextlib import closing
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from common import get_input
 
closing_brackets = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<"
}

closing_brackets_scoring = {
    "(" : 1,
    "[" : 2,
    "{" : 3,
    "<" : 4
}

counter =  {
    ")" : 0,
    "]" : 0,
    "}" : 0,
    ">" : 0
}


def find_not_matching_bracket(row):
    for i in range(1,len(row)):
        if row[i] in closing_brackets.keys():
            if closing_brackets[row[i]] != row[i-1]:
                counter[row[i]] += 1    
                return True
            else:
                row = row[0 : i-1 : ] + row[i + 1 : :]
                return find_not_matching_bracket(row)

def get_only_open_brackets(row):

    for i in range(1, len(row)):         
        if row[i] in closing_brackets.keys():
            if closing_brackets[row[i]] == row[i-1]:
                row = row[0 : i-1 : ] + row[i + 1 : :]
                sum = row.count("]") + row.count(")") + \
                        row.count(">") + row.count("}") 
                if sum > 0:
                    return get_only_open_brackets(row)
                else:
                    return row

def get_values(brackets_list):
    values_list = []
    for i in brackets_list:
        values_list.append(closing_brackets_scoring[i])
    return values_list


def get_score(values_list):
    score = 0
    for i in values_list:
        score = score * 5 + i
    return score


input_data = get_input.get_input_data()

scores = []

for row in input_data:
    if not find_not_matching_bracket(row):
        
        new_row = get_only_open_brackets(row.strip())
        closing_brackets_list = new_row[::-1]
        brackets_values = get_values(closing_brackets_list)
        result = get_score(brackets_values)
        scores.append(result)

sorted_scores = sorted(scores)
index = round(len(sorted_scores) / 2) - 1

print(sorted_scores[index])
