'''
Created on May 7, 2013

@author: debajyoti
'''

import numpy as np
import matplotlib.pyplot as plt


numPoints = 10
outPoints = 1000
numEpochs = 1000
showN = 20 #used to plot every Nth-epoch
averageIteration = 0
averageDistance = 0
averageError = 0
averageEin=0
averageEout = 0
tol =0.01
learning_rate = 0.01


plt.ion();
plt.axis([-1, 1, -1, 1])
plt.axes().set_aspect('equal')
plt.show()


lineX = np.random.uniform(-1, 1, 2)
lineY = np.random.uniform(-1, 1, 2)

def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m
 

#form the line using 2-point form method 
def makeLine(x):
    return lineX[1] + (lineY[1] - lineX[1]) / (lineY[0] - lineX[0]) * ( x - (lineX[0]))
 
#plot the line, red
plt.plot( [-1,1],[makeLine(-1),makeLine(1)] ,'r')

def classifyPoint(point):
    if point[2] > makeLine(point[1]):
        return 1
    else:
        return -1




if __name__ == '__main__':
    pass