'''
Created on May 21, 2013

@author: debajyoti
'''

import numpy as np

e1 = 0
e2 = 0
e = 0

for i in range(1,1000):
    e1new = np.random.uniform(0,1)
    e2new = np.random.uniform(0,1)
    e  += min(e1new,e2new)
    e1 += e1new
    e2 += e2new
    

print e1/1000
print e2/1000
print e/1000

if __name__ == '__main__':
    pass