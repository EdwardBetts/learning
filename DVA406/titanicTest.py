'''
Created on Feb 21, 2013

@author: debajyoti
'''

import csv as csv
import numpy as np

#open file - test set
test_file_object = csv.reader(open('D:/IntelligentSystems/kaggle/Train/Train.csv','rb'))
#header = test_file_object.next() #removes headers
print "file opened successfully"

open_file_object = csv.writer(open('D:/IntelligentSystems/kaggle/Train/TrainHeaders.csv', 'wb'))

#split the big file into parts
k = 0;
for row in test_file_object:
    if k < 10 :
        open_file_object.writerow(row)
    k= k+1

'''
for row in test_file_object:
    if row[2] == "female":
        row.insert(0,'1')        
    else:
        row.insert(0,'0')        
        
    open_file_object.writerow(row)
'''        

if __name__ == '__main__':
    pass