'''
Created on Mar 17, 2013

@author: debajyoti
'''

import csv as csv
import numpy as np

#lists
level6=[]
level5=[]
level4=[]
level3=[]
level2=[]
level1=[]
root =[]

#dictionaies
dlevel6={}
dlevel5={}
dlevel4={}
dlevel3={}
dlevel2={}
dlevel1={}
droot ={}


branch=[root,level1,level2,level3,level4,level5,level6]

#mapping child as dict value
dict=[droot,dlevel1,dlevel2,dlevel3,dlevel4,dlevel5,dlevel6]

def run():
    rfile = csv.reader(open('D:/IntelligentSystems/kaggle/Location_Tree_separated.csv','rb'))
    data = []
    
    count =0
    for row in rfile:
        data.append(row);
        count = count +1
    print count
    
    #file for writing
    #wdata =[]
    #file = csv.writer(open('D:/IntelligentSystems/kaggle/Location_Tree_branches.csv','wb'))
    
    for row in data:
        for index in range(0, np.size(row)):
            '''
            if index>0 :
                if row[index-1] in branch[index-1]:
                    dict[index-1][index-1]=branch[index-1]
            '''
            if row[index] not in branch[index]:
                branch[index].append(row[index])
    
    '''
    print branch[0]
    print branch[1]
    print branch[2]
    print branch[3]
    print branch[4]
    print branch[5]
    print branch[6]
    '''
    
    print np.size(branch[0])
    print np.size(branch[1])
    print np.size(branch[2])
    print np.size(branch[3])
    print np.size(branch[4])
    print np.size(branch[5])
    print np.size(branch[6])
    
    for row in data:
        for k in level6:
            if k in row:
                for g in level5:
                    if g in row:
                        dlevel5[g] = k
        for k in level5:
            if k in row:
                for g in level4:
                    if g in row:
                        dlevel4[g] = k
        for k in level4:
            if k in row:
                for g in level3:
                    if g in row:
                        dlevel3[g] = k
        for k in level3:
            if k in row:
                for g in level2:
                    if g in row:
                        dlevel2[g] = k
        for k in level2:
            if k in row:
                for g in level1:
                    if g in row:
                        dlevel1[g] = k
        for k in level1:
            if k in row:
                for g in root:
                    if g in row:
                        droot[g] = k    
        
    
                
        
        
        
    '''
    print dict[0]
    print dict[1]
    print dict[2]
    '''
    
    print droot
    print dlevel1
    
    '''
    for row in branch:
        file.writerow(row)        
    '''    
    

if __name__ == '__main__':
    run()