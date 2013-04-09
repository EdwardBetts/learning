'''
Created on Mar 14, 2013

@author: debajyoti
'''

import numpy as np   
import matplotlib.pyplot as plt  
import csv as csv

rfile= csv.reader(open('D:/IntelligentSystems/kaggle/mapCategory.csv','rb'))

dat=[]
for row in rfile:
    dat.append(row)

dat=np.array(dat)

x, y = dat[0::,2], dat[0::,1]

heatmap, xedges, yedges = np.histogram2d(x, y)  
extent = [xedges[0], xedges[10000], yedges[0], yedges[30]]  
plt.clf()  
plt.imshow(heatmap, extent=extent)  
plt.show() 

if __name__ == '__main__':
    pass