'''
Created on Feb 21, 2013

@author: debajyoti
'''
import csv as csv
import numpy as np

#open file - training set
csv_file_object = csv.reader(open('D:/IntelligentSystems/kaggle titanic/train.csv','rb'))
header = csv_file_object.next()
print "file opened successfully"

#read data
data = []
for row in csv_file_object :
    data.append(row)
    
#convert list to array
data = np.array(data)

women_only_stats = data[0::,3] == "female"
men_only_stats = data [0::,3] != "female"

women_onboard = data[women_only_stats,0].astype(np.float) 
men_onboard = data[men_only_stats,0].astype(np.float)

proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print 'Proportion of women who survived is %s' % proportion_women_survived

print 'Proportion of men who survived is %s' % proportion_men_survived

fare_ceiling = 40
data[data[0::,8].astype(np.float) >= fare_ceiling, 8] = fare_ceiling-1.0
fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size
number_of_classes = 3 #There were 1st, 2nd and 3rd classes on board 
# Define the survival table
survival_table = np.zeros((2, number_of_classes, number_of_price_brackets))

for i in xrange(number_of_classes):       #search through each class
    for j in xrange(number_of_price_brackets):   #search through each price
        women_only_stats = data[                      #Which element           
                         (data[0::,3] == "female")    #is a female
                       &(data[0::,1].astype(np.float) #and was ith class
                             == i+1)                                       
                       &(data[0:,8].astype(np.float)  #was greater 
                            >= j*fare_bracket_size)   #than this bin              
                       &(data[0:,8].astype(np.float)  #and less than
                            < (j+1)*fare_bracket_size)#the next bin    
                          , 0]                        #in the 1st col                           
                                                                                                 


        men_only_stats = data[                            #Which element           
                         (data[0::,3] != "female")    #is a male
                       &(data[0::,1].astype(np.float) #and was ith class
                             == i+1)                                       
                       &(data[0:,8].astype(np.float)  #was greater 
                            >= j*fare_bracket_size)   #than this bin              
                       &(data[0:,8].astype(np.float)  #and less than
                            < (j+1)*fare_bracket_size)#the next bin    
                          , 0]
        
        survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float)) #Women stats
        survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float)) #Men stats

            
survival_table[ survival_table != survival_table ] = 0.

#survival_table[ survival_table < 0.5 ] = 0
#survival_table[ survival_table >= 0.5 ] = 1

print survival_table


if __name__ == '__main__':
    pass