'''
Created on Apr 5, 2013

@author: debajyoti
'''

import pylab
import random

#initialise and draw line
x1 = random.randint(-1,1)
x2 = random.randint(-1,1)
m=x2/x1    
#pylab.plot(x1)
#pylab.plot(x2)
print x1
print x2
x = [x1,x2]
y=m*x
print y

#initialise and draw 10 random points
d=[]

for i in range(1,11):
    d.append(random.randint(-1,1))

pylab.plot(d, hold=True)
pylab.plot(y, hold=True)

pylab.show()

