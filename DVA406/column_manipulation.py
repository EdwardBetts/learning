'''
Created on Mar 8, 2013

@author: debajyoti
'''

import csv as csv

f1 = csv.reader(open('C:/Users/debajyoti/Downloads/267847/Valid.csv','rb'))

data = []
for row in f1:
    row.insert(1,33316.5)
    data.append(row)

f1 = csv.writer(open('C:/Users/debajyoti/Downloads/267847/out.csv','wb'))
for row in data: 
    f1.writerow(row)
print 'done'

if __name__ == '__main__':
    pass