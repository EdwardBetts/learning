'''
Created on Apr 14, 2013

@author: debajyoti
'''

import numpy as np

numPoints = 1000
outPoints = 1000
numEpochs = 1000
showN = 20
averageIteration = 0
averageEin = 0
averageEin2 = 0
averageEout = 0
averageErrorPoints = 0

def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

def target(x1,x2):
    #return ((x1) + (x2) - 0.6)
    return (np.square(x1) + np.square(x2) - 0.6)

def classifyPoint(p):
    res = target(p[1],p[2])
    val = np.sign(res)
    return val

for i in range(numEpochs):
    
    #generate data
    points = np.random.uniform(-1,1,(numPoints,2))
    zeros = np.ones( (numPoints,1) )
    points = np.append(zeros, points, axis = 1)
    
    
    #add more dimensions
    '''
    val4 = [] 
    val5 = []
    val6 = []
    
    for p in points:
        val4.append(p[1]*p[2]) 
        val5.append(np.square(p[1]))
        val6.append(np.square(p[2]))
    
    points = np.append(val4, points, axis = 4)
    points = np.append(val5, points, axis = 5)
    points = np.append(val6, points, axis = 6)
    
    '''
    
    X = makeMatrix(numPoints, 3)
    Y = makeMatrix(numPoints, 1)
    X2 = makeMatrix(numPoints, 6)
    
    i = 0
    for p in points:
            for j in range(0,3):
                X[i][j]=p[j]
                X2[i][j]=p[j]
                X2[i][3]= X[i][1]*X[i][2]
                X2[i][4]= X[i][1]*X[i][1]
                X2[i][5]= X[i][2]*X[i][2]
            Y[i] = classifyPoint(p)
            i += 1
           
    #flip 10% data randomly to introduce noise
    noise = numPoints/10
    c = []
    for i in range(noise):
        k = np.random.randint(1,numPoints) 
        if k not in c:
            c.append(k)
            Y[k] = (-1)*Y[k]
       
    #calculate pseudo-inverse of matrix and weights
    invX = np.linalg.pinv(X)
    invZ = np.linalg.pinv(X2)
    
    W =[]
    W2 = []
#    for each in invX:
#        k=0
#        for i in range(numPoints):
#            k += each[i]*Y[i]
#        W.append(k)
#    
    W = np.dot(invX, Y)
    W2 = np.dot(invZ,Y)
    
    
    roundEin = 0
    errorPoints = 0
    for p in points:
        a = classifyPoint( p )
        b = np.sign(np.dot(W, p))
        if b != a:
            #print np.dot(W, p)
            roundEin += np.abs((b-a)/2)
            errorPoints += 1
    #print roundEin
    averageEin += (roundEin/(numPoints*1.0))
    averageErrorPoints += errorPoints/(numPoints * 1.0)
    
    roundEin2 = 0
    errorPoints2 = 0
    for p in X2:
        a = classifyPoint( p )
        b = np.sign(np.dot(W2,p))
        if b != a:
            roundEin2 += np.abs((b-a)/2)
            errorPoints2 += 1
    averageEin2 += (roundEin2/(numPoints*1.0))
    #out of sample error
    newPoints = np.random.uniform(-1,1,(outPoints,2))
    newZeros = np.ones( (outPoints,1) )
    newPoints = np.append(newZeros, newPoints, axis = 1)
    
    X3 = makeMatrix(numPoints, 6)
    
    i = 0
    for p in points:
            for j in range(0,3):
                X3[i][j]=p[j]
                X3[i][3]= X3[i][1]*X3[i][2]
                X3[i][4]= X3[i][1]*X3[i][1]
                X3[i][5]= X3[i][2]*X3[i][2]
            i += 1
    
    roundEout = 0
    for p in X3:
        if np.sign( np.dot(W2, p) ) != classifyPoint( p ):
            roundEout += 1
    #print roundEout
    averageEout += (roundEout/(outPoints*1.0))
    

print ("Average Ein :"+ str(averageEin/numEpochs))
print ("Average Ein 2:"+ str(averageEin2/numEpochs))
print ("Average Eout :"+ str(averageEout/numEpochs))
print ("Tolerance :" + str(np.absolute(averageEin-averageEout)/numEpochs))
print("Average error :" + str(averageErrorPoints/numEpochs))