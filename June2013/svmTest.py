import numpy as np
from sklearn.svm import SVC
X = np.array([[1,0],[0,1],[0,-1],[-1,0],[0,2],[0,-2],[-2,0]])
y= np.array([-1,-1,-1,1,1,1,1])
Z=[]
def my_kernel(x, y):
    return np.square(1+np.dot(x.T,y))
    
clf = SVC(kernel=my_kernel)
clf.fit(X,y)
print clf.n_support_