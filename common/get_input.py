
import os
import sys
import pandas as pd

def get_item(item):
    
    if "\n" in item and len(item) > 1:
        return item[:item.find('\n')]
    elif len(item) > 1:
        return item

def get_input_data():

    f = open(os.path.join(sys.path[0], 'Input Data.txt')).readlines()
    data = pd.DataFrame(f)
    data = data.applymap(get_item)[0]
    return data