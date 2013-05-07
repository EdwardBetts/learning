'''
Created on Apr 30, 2013

@author: debajyoti
'''
import math
import numpy as np


dvc = 10
N1 = 40
N2 = 42
N3 = 44
N4 = 46
N5 = 48
tol = 0.05

#points1 = np.random.uniform(-1,1,(N1))
#points2 = np.random.uniform(-1,1,(N2))
#points3 = np.random.uniform(-1,1,(N3))
#points4 = np.random.uniform(-1,1,(N4))
#points5 = np.random.uniform(-1,1,(N5))


def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

f1= 0
f2= 0
f3= 0
f4= 0
f5= 0
for i in range (0,dvc):
    f1 += nCr(2*N1,i)
    f2 += nCr(2*N2,i)
    f3 += nCr(2*N3,i)
    f4 += nCr(2*N4,i)
    f5 += nCr(2*N5,i)

print f1
print f2
print f3
print f4
print f5


if __name__ == '__main__':
    pass