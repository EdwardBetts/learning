'''
Created on Apr 12, 2013

@author: debajyoti
'''

import numpy as np
import matplotlib.pyplot as plt
 
#run with more numPoints and less numEpochs for better visualization 
numPoints = 10
outPoints = 1000
numEpochs = 1000
showN = 20 #used to plot every Nth-epoch
averageIteration = 0
averageDistance = 0
averageError = 0
averageEin=0
averageEout = 0

#turn on interactive mode 
#plt.ion()
 
#plot basic axes 
#plt.axis([-1, 1, -1, 1])
#plt.axes().set_aspect('equal')
#plt.show()
 
 
## generate 2 random points to form a line
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
#plt.plot( [-1,1],[makeLine(-1),makeLine(1)] ,'b')


#classify as 1 or -1
def classifyPoint(point):
    if point[2] > makeLine(point[1]):
        return 1
    else:
        return -1
 
def getDistance(point):
    return (point[2] - makeLine(point[1])) 

epoch = 0
X = makeMatrix(numPoints, 3)
Y = makeMatrix(numPoints, 1)

while epoch < numEpochs :
     
    ## generate sample points
    points = np.random.uniform(-1,1,(numPoints,2))
    zeros = np.ones( (numPoints,1) )
    points = np.append(zeros, points, axis = 1)
    
    #print points 
    ''' 
    for p in points:
        if classifyPoint(p) == 1:
            if(epoch % showN == 0):
                plt.plot( p[1], p[2], 'bo' )
        else:
            if(epoch % showN == 0):
                plt.plot( p[1], p[2], 'go' )
 
    plt.draw()
    '''
    
    
    #linear regression
    i = 0
    for p in points:
            for j in range(0,3):
                X[i][j]=p[j]
            Y[i] = classifyPoint(p)
            i += 1
    
    #calculate pseudo-inverse of matrix and weights
    invX = np.linalg.pinv(X)
    
    W =[]
    for each in invX:
        k=0
        for i in range(numPoints):
            #print each[i]
            #print Y[i]
            k += each[i]*Y[i]
        W.append(k)
            
#    x = np.array( [-1,1] )
#    h = (-W[1]/W[2] * x) - (W[0] / W[2])
#    plt.plot( x, h , 'g' )
#    plt.draw()

    #calculate in-sample error
#    roundEin = 0    
#    for p in points:
#        if np.sign( np.dot(W, p) ) != classifyPoint( p ):
#            roundEin += 1
#    averageEin += (roundEin/(numPoints*1.0))
    
    
    #module for checking out-of-sample error
    '''
    #out of sample test
    roundEout = 0
    newPoints = np.random.uniform(-1,1,(outPoints,2))
    outZeros = np.ones( (outPoints,1) )
    newPoints = np.append(outZeros, newPoints, axis = 1)

    for p in newPoints:
        if np.sign( np.dot(W, p) ) != classifyPoint( p ):
            roundEout += 1
    #print roundEout
    averageEout += (roundEout/(outPoints*1.0))
    '''
    
    
    #initialize weight vector
    #w = np.zeros( 3 )
    
    iteration = 0
    done = False
    while not done:
        iteration += 1
        wrongPoints = 0 #can be used to find averageError
        
        #check classification of points, update weights for the first one found to be wrong
        for p in points:
            w = W
            if np.sign( np.dot(w, p) ) != classifyPoint( p ):
                w = np.add( w, classifyPoint( p ) * p )  #assuming learning rate = 1
                #d = getDistance(p)
                #print ("distance :"+str(d))
                #distance += d
                wrongPoints += 1
                break
        
        if wrongPoints == 0:
            print ("iterations :"+str(iteration))
            averageIteration += iteration; 
            averageError += wrongPoints
            done = True
 
 
        # drawing every Nth final function
        if(epoch % showN == 0):
            print("epoch :"+ str(epoch))
            #x = np.array( [-1,1] )
            #plt.plot( x, -w[1]/w[2] * x - w[0] / w[2] , 'r' )
            #plt.draw()
    
    epoch += 1
    
    #averageDistance = (distance*distance)/ (numPoints*1.0)
    #print ("Average distance :"+ str(averageDistance))

print ("Average Iteration :"+ str(averageIteration/numEpochs))
print ("Average Error :"+ str(averageError/numEpochs))
print ("Average Ein :"+ str(averageEin/numEpochs))
print ("Average Eout :"+ str(averageEout/numEpochs))
#print ("Average distance :"+ str(averageDistance/numEpochs))