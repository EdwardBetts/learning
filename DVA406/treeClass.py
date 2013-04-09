'''
Created on Mar 18, 2013

@author: debajyoti
'''

import csv as csv
import numpy as np

data = []

class tree:
    def _init_(self):
        pass

def read():
    rfile = csv.reader(open('D:/IntelligentSystems/kaggle/Location_Tree_separated.csv','rb'))
    count =0
    for row in rfile:
        data.append(row);
        count = count +1
    print count
    data= np.array(data)

def run():
    read()

if __name__ == '__main__':
    run()