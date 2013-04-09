'''
Created on Mar 6, 2013

@author: debajyoti
'''

import math
import random
#import fractions as fr
import csv as csv
import numpy as np
import pycallgraph



random.seed(0)

def rand(a, b):
    return (b-a)*random.random() + a

def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
    return math.tanh(x)

# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    return 1.0 - y**2

class NN:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh = nh
        self.no = no
        '''
        print "neurons = "
        print self.ni
        print self.nh
        print self.no
        '''
        # activations for nodes
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no
        
        # create weights matrix
        self.wi = makeMatrix(self.ni, self.nh)
        #print "wi =" 
        #print self.wi
        self.wo = makeMatrix(self.nh, self.no)
        #print "wo =" 
        #print self.wo

        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)
        '''        
        print "wi random =" 
        print self.wi
        print "wo random =" 
        print self.wo
        '''
                
        # last change in weights for momentum   
        self.ci = makeMatrix(self.ni, self.nh)
        #print "ci =" 
        #print self.ci
        self.co = makeMatrix(self.nh, self.no)
        #print "co =" 
        #print self.co

    def update(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')
        '''

        # input activations
        for i in range(self.ni-1):
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                #print self.ai[i]
                #print self.wi[i][j]
                kin = float(self.ai[i])
                sum = sum + (kin * self.wi[i][j])
            self.ah[j] = sigmoid(sum)

        # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)
        
        '''
        #inputs
        for i in range(self.ni-1):
            self.ai[i] = inputs[i]
        
        #hidden
        for i in range(self.nh):
            sum = 0.0
            for j in range(self.ni):
                sum = sum + (self.wi[j][i]*float(self.ai[j]))
            self.ah[i] = sum    #removed sigmoid
        
        #output
        for i in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + (self.wo[j][i]*self.ah[j])
            self.ao[i] = sum
            
        
        return self.ao[:]


    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')
        
        
        '''
        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        
        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error
        
            
        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                #print hidden_deltas[j]
                #print self.ai[i]
                kin = np.float(self.ai[i])
                change = hidden_deltas[j]*kin
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.ao[k])**2
        error = error/len(targets)
        '''
        
        #output error
        outerror = [0.0]*self.no
        for k in range(self.no):
            outerror[k] = targets[k]-self.ao[k]
        
        #hidden error
        hiderror = [0.0]*self.nh
        for j in range(self.nh):
            er = 0.0
            for k in range(self.no):
                er = er + (outerror[k]*self.wo[j][k])
            hiderror[j] = er
        
        #update output weights
        for j in range(self.nh):
            for k in range(self.no):
                er = outerror[k]*self.ah[j]
                self.wo[j][k]=self.wo[j][k]  + N*er #not using momentum yet
                # what is "c_" ??
        
        #update hidden weights
        for i in range(self.ni):
            for j in range(self.nh):
                if(float(self.ai[i])):
                    er = hiderror[j]*float(self.ai[i])    
                self.wi[i][j] = self.wi[i][j] + N*er
        
        error = 0.0
        for k in range(len(targets)):
            error = error + (targets[k]-self.ao[k])
        error = error/len(targets)
        return error    #return average squared mean error
       
    def test(self, patterns):
        write_file_object = csv.writer(open('D:/IntelligentSystems/kaggle/col/outputResultNew17.csv', 'wb'))
        for p in patterns:
            val = self.update(p[0])
            print val
            '''
            val2=p[1]
            print 'val2 =' 
            print  val2 #float(fr.Fraction("".join(val2)))
            #upVal = float(val2.strip("'")) + float(val.strip("'"))
            upVal = map(sum, zip(val,val2))
            #z2 = makeMatrix(1,40663,5000.00)
            #upVal2 = map(sum,zip(upVal*195000,z2))
            '''
            write_file_object.writerow(val)
            print(p[0], '->', val)
        
        #for p in patterns:
            #print(p[0], p[1])
            
        
        

    def weights(self):
        print('Input weights:')
        for i in range(self.ni):
            print(self.wi[i])
        print()
        print('Output weights:')
        for j in range(self.nh):
            print(self.wo[j])

    def train(self, patterns, iterations=200, N=0.3, M=0.5):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                #lowest = 1.0
                error = self.backPropagate(targets, N, M)
                '''
                if(error<lowest):
                    lowest = error
                    #self.weights()
                '''
            if i % 10 == 0:
                print('error %-.5f' % error)
                print 'epoch =' 
                print i


def prep(pat2):
    test_file_object = csv.reader(open('D:/IntelligentSystems/kaggle/col/DistinctValidationData.csv','rb'))
    header = test_file_object.next() #removes headers
    print "file opened successfully"
    data = []
    for row in test_file_object :
        data.append(row)
    
    #convert list to array
    data = np.array(data)
    p1=[]
    p2=[]

    for row in data:
        k = row[1],row[2],row[3]
        p1.append(k)
        avg = 33084
        g = (np.float(avg)-5000)/195000
        h=[g]
        p2.append(h)       
        
        

    i=0  
          
    for row in p1:
        p = row ,p2[i]
        pat2.append(p)
        
    pat2 = np.array(pat2)

def run():
    train_file_object = csv.reader(open('D:/IntelligentSystems/kaggle/col/merged.csv','rb'))
    header = train_file_object.next() #removes headers
    print "file opened successfully"
    data = []
    for row in train_file_object :
        data.append(row)
    
    #convert list to array
    data = np.array(data)
    p1=[]
    p2=[]

    for row in data:
        if(str.isdigit(row[4])):
            k = row[1],row[2],row[3]
            p1.append(k)
            g = (np.float(row[4])-5000)/195000
            h=[g]
            p2.append(h)       
        
        

    i=0  
    pat = []      
    for row in p1:
        p = row,p2[i]
        pat.append(p)
        
    pat = np.array(pat)
    pat2 = []    
    prep(pat2)
            
    
    n = NN(3, 3, 1)
    # train it with some patterns
    n.train(pat)
    # test it
    n.test(pat2)
    #n.weights()
        

if __name__ == '__main__':
    pycallgraph.start_trace()
    run()
    pycallgraph.make_dot_graph('D:/IntelligentSystems/kaggle/linNN.png')