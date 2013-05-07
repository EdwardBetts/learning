'''
Created on Apr 8, 2013

linearly separate random points on the plane [-1,1]X[-1,1]
 
@author: debajyoti
'''

import numpy as np
import matplotlib.pyplot as plt
 
#run with more numPoints and less numEpochs for better visualisation 
numPoints = 10
numEpochs = 100
showN = 20
averageIteration = 0

#turn on interactive mode 
plt.ion()

#plot basic axes 
plt.axis([-1, 1, -1, 1])
plt.axes().set_aspect('equal')
plt.show()
 
 
## generate 2 random points to form a line
lineX = np.random.uniform(-1, 1, 2)
lineY = np.random.uniform(-1, 1, 2)
 

#form the line using 2-point form method 
def makeLine(x):
    return lineX[1] + (lineY[1] - lineX[1]) / (lineY[0] - lineX[0]) * ( x - (lineX[0]))
 
#plot the line, red
plt.plot( [-1,1],[makeLine(-1),makeLine(1)] ,'b')
#ax=fig.add_subplot(2,2,1)

#classify as 1 or -1
def classifyPoint(point):
    if point[2] > makeLine(point[1]):
        return 1
    else:
        return -1
 
 

epoch = 0
while epoch < numEpochs :
     
    ## generate sample points
    points = np.random.uniform(-1,1,(numPoints,2))
    zeros = np.ones( (numPoints,1) )
    points = np.append(zeros, points, axis = 1)
 
    for p in points:
        if classifyPoint(p) == 1:
            if(epoch % showN == 0):
                plt.plot( p[1], p[2], 'bo' )
        else:
            if(epoch % showN == 0):
                plt.plot( p[1], p[2], 'go' )
 
    plt.draw()
 
    #initialize weight vector
    w = np.zeros( 3 )
 
    iteration = 0
 
    done = False
    while not done:
        iteration += 1
        wrongPoints = 0
        print ("Weights :" +str(w))
        #check classification of points, update weights for the first one found to be wrong
        for p in points:
            if np.sign( np.dot(w, p) ) != classifyPoint( p ):
                w = np.add( w, classifyPoint( p ) * p )  
                wrongPoints += 1
                break
        if wrongPoints == 0:
            print ("iterations :"+str(iteration))
            averageIteration += iteration; 
            done = True
 
 
            # drawing every Nth final function
            if(epoch % showN == 0):
                #print("epoch :", str(epoch))
                x = np.array( [-1,1] )
                plt.plot( x, -w[1]/w[2] * x - w[0] / w[2] , 'r' )
                plt.draw()
    
    epoch += 1

print ("Average Iteration :"+ str(averageIteration/numEpochs))