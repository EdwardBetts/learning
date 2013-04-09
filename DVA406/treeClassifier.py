'''
Created on Mar 14, 2013

@author: debajyoti
'''

import csv as csv
import numpy as np



'''
level4.append(level5)
level3.append(level4)
level2.append(level3)
level1.append(level2)
root.append(level1)
'''


def read():
    rfile = csv.reader(open('D:/IntelligentSystems/kaggle/Location_Tree.csv','rb'))
    data = []
    index =0
    count = 0
    for row in rfile:
        data.append(row);
        count = count +1
    
    print count
    tree = []*count
    
    
    '''
    for row in data:
        g=str(row).strip('[]')
        k= g.split('~')
        pos=0        
        for i in k:
            if k[pos] not in branch[pos]:
                #print k[pos]
                #print tree[pos]
                branch[pos].append(k[pos])
                print k[pos]
                pos = pos+1
                
        #print k
        #print tree
        print branch
        index=index+1
        #tree[index]=branch
        
        if index >5:
            break
        
        
    #print tree

    '''
    wdata =[]
    file = csv.writer(open('D:/IntelligentSystems/kaggle/Location_Tree_separated.csv','wb'))
    for row in data:
        g=str(row).strip('[]')
        k= g.split('~')
        wdata.append(k)
        
    
    for row in wdata:        
        file.writerow(row)
    

if __name__ == '__main__':
    #pycallgraph.start_trace()
    read()
    #pycallgraph.make_dot_graph('D:/IntelligentSystems/kaggle/treeClassifierTest.jpeg', format='jpg', tool='neato', stop='true')
