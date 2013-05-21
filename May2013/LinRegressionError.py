'''
Created on May 7, 2013

@author: debajyoti
'''

import numpy as np

sig = 0.1
var = np.square(sig)
d = 8
Na = 10
Nb = 25
Nc = 100
Nd = 500
Ne = 1000

print (var*(1-(np.float32(d+1)/Na)))
print (var*(1-(np.float32(d+1)/Nb)))
print (var*(1-(np.float32(d+1)/Nc)))
print (var*(1-(np.float32(d+1)/Nd)))
print (var*(1-((d+1)/Ne)))

if __name__ == '__main__':
    pass