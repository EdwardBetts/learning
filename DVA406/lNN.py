'''
Created on Mar 1, 2013

@author: debajyoti
'''

import csv as csv
import neurolab as nl   
import numpy as np
#import math

train_file_object = csv.reader(open('D:/IntelligentSystems/kaggle/col/merged.csv','rb'))
header = train_file_object.next() #removes headers
print "file opened successfully"
data = []
for row in train_file_object :
    data.append(row)
    
#convert list to array
data = np.array(data)
p1=[]
p2=[]
c=0

for row in data:
    if(str.isdigit(row[4])):
        k = row[1],row[2],row[3]
        p1.append(k)
        g = (np.float(row[4])-5000)/95000
        p2.append(g)        
    else:
        c = c+1;
        
    
i = 1
    
for row in p1:
    if i in range(5,20) :
        print i
        print row
        print p2[i]
    i = i+1

net = nl.net.newff([[0,29],[0,1],[0,1]], [3,1])
print net.ci
print net.co
print net.connect
print len(net.layers)
error = net.train(p1, p2, epochs=500, show=100, goal=0.02)
print error

if __name__ == '__main__':
    pass