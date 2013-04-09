'''
Created on Mar 12, 2013

@author: debajyoti
'''

import numpy as np
import csv as csv
import sklearn
#from sklearn import ensemble - it crashes stuff, use Tobias's laptop

#from sklearn.ensemble import RandomForestClassifier

#training data
train_file_object = csv.reader(open('D:/IntelligentSystems/kaggle/col/merged.csv','rb'))
header = train_file_object.next() #removes headers
print "file opened successfully"

train_data = []
for row in train_file_object :
    train_data.append(row)

train_data = np.array(train_data)

#test data
test_file_object = csv.reader(open('D:/IntelligentSystems/kaggle/col/DistinctValidationData.csv','rb'))
header = test_file_object.next() #removes headers
print "file opened successfully"

test_data = []
for row in test_file_object :
    test_data.append(row)
test_data = np.array(test_data)

#test_data = np.delete(test_data,[1,6,8],1)

print 'Training '


forest= [] #remove or comment before running
#forest = ensemble.RandomForestClassifier(n_estimators=100)

forest = forest.fit(train_data[0::,1:3],train_data[0::,4])


print 'Predicting'
output = forest.predict(test_data[0::,1::])

open_file_object = csv.writer(open('D:/IntelligentSystems/kaggle/col/trialForest17.csv', "wb"))
test_file_object = csv.reader(open('D:/IntelligentSystems/kaggle/col/DistinctValidationData.csv','rb', 'rb')) #Load in the csv file

test_file_object.next()

i = 0
for row in test_file_object:
    row.insert(0,output[i].astype(np.uint8))
    open_file_object.writerow(row)
    i += 1





if __name__ == '__main__':
    pass