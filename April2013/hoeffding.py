'''
Created on Apr 11, 2013

@author: debajyoti
'''

import random as rand
f= open('D:\IntelligentSystems\EclipsePortable\Data\workspace\April2013\hoeffdingRes2.txt','wb')

def decide():
    return rand.randint(1,2) #1 for heads, 2 for tails


def flip():
    fHead=0
    fTail=0
    for i in range(0,11):
        filpRes= decide()
        if filpRes == 1:
            #print 'H'
            fHead+= 1
        else :
            #print "T"
            fTail+= 1
    #print ("fHead :" + str(fHead));
    return fHead
    


#do for each coin
def run():
    coin =0
    fMin=1
    fC1=0
    fRand=0
    fRes = 0.0
    randomCoin= rand.randint(0,1000)
    while coin < numCoins:
        fRes =flip()
        #print ("fRes :"+ str(fRes))
        fResNorm = fRes/10.0
        #print ("fResNormalised :"+ str(fResNorm))
        if fResNorm < fMin:
            fMin = fResNorm
        if coin ==0 :
            fC1 = fResNorm
        if coin == randomCoin:
            fRand = fResNorm
        coin += 1
    '''
    print ("first :"+ str(fC1))
    print ("random :"+ str(fRand))
    print ("minimum :"+ str(fMin))
    '''
    f.write("first :"+ str(fC1)+"\n")
    f.write("random :"+ str(fRand)+"\n")
    f.write("minimum :"+ str(fMin)+"\n\n")
    return (fC1,fMin,fRand)
    
        
        
if __name__ == '__main__':
    numCoins = 1000
    numEpochs = 100000
    avgC1=0
    avgCrand=0
    avgCmin=0
    cMin=0
    epoch = 0
    while epoch < numEpochs:
        cMin=10
        (a,b,c) = run()
        epoch += 1
        avgC1 += a
        avgCmin += b
        avgCrand += c
        print ("epoch :" + str(epoch))
    
    print ("average first :" + str(avgC1/numEpochs))
    print ("average random :" + str(avgCrand/numEpochs))
    print ("average minimum :" + str(avgCmin/numEpochs))
    f.write("average first :" + str(avgC1/numEpochs) +"\n"+ "average random :" + str(avgCrand/numEpochs) +"\n"+ "average minimum :" + str(avgCmin/numEpochs))
    f.close()