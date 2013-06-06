import numpy as np
from sklearn.svm import SVC

num=0
numEpoch = 10000
for epoch in range(numEpoch):

    x1 = np.random.uniform(-1,1,100)
    x2 = np.random.uniform(-1,1,100)

    def classify(x1,x2):
        return np.sign(x2-x1+0.25*(np.sin(np.pi*x1)))
    
    y = []
    X = []
    for i in range(0,100):
        d=classify(x1[i],x2[i])
        X.append([x1[i],x2[i]])
        y.append(d)
    clf = SVC(gamma=1.5, kernel='rbf')
    clf.fit(X,y)
    error = 0
    for i in range(0,100):
        error += y[i]-clf.predict(X[i])
    
    if( error == 0):
        num += 1   

print np.float(num)/np.float(numEpoch)