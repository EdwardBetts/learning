'''
Created on Feb 26, 2013

@author: debajyoti
'''

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('D:/IntelligentSystems/kaggle/col/salary.txt','rb'))
print "file opened successfully"

open_file_object = csv.writer(open('D:/IntelligentSystems/kaggle/col/salary.csv', 'wb'))

data = []
for row in csv_file_object :
    data.append(row)
    
#data = np.array(data)

for row in data :
    open_file_object.writerow(row)
    
print "go check"
    

if __name__ == '__main__':
    pass