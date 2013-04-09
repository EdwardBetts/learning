'''
Created on Mar 2, 2013

@author: debajyoti
'''
import csv as csv
import numpy as np

read_file_object = csv.reader(open('D:/IntelligentSystems/kaggle/col/outputResult.csv','rb'))

data=[]
for row in read_file_object:
    data.append(row) 

#data= np.array(data)

#z2 = [5000]*len(data)


def makeMatrix(I, J, fill=1.00):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

z2 = makeMatrix(1,len(data),5000.00)
print z2

i=0

data = np.array(data)
z2 = np.array(z2)
print z2
print data

'''
for row in data:
    #print data[0]
    z2[i] = z2[i] +data[i]
    #row.insert(map(sum,zip(data[0]*95000, z2)))
    i=i+1
'''

print "res ="
print   np.add(data,z2)

write_file_object = csv.writer(open('D:/IntelligentSystems/kaggle/col/validRes.csv', 'wb'))
for row in data:
    write_file_object.writerow(row)
     


if __name__ == '__main__':
    pass