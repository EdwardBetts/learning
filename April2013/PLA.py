'''
Created on Apr 5, 2013

@author: debajyoti
'''

import random

x1 = random.randint(-1,1)
x2 = random.randint(-1,1)
y1 = random.randint(-1,1)
y2 = random.randint(-1,1)

threshold = 0.5
learning_rate = 1.0
weights = [0, 0, 0]

d=[]

for i in range(1,11):
    d.append(random.randint(-1,1),random.randint(-1,1))

training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]
 
def dot_product(values):
    return sum(value * weight for value, weight in zip(values, weights))
 
while True:
    print '-' * 60
    error_count = 0
    for input_vector, desired_output in training_set:
        print weights
        result = dot_product(input_vector) > threshold
        error = desired_output - result
        if error != 0:
            error_count += 1
            for index, value in enumerate(input_vector):
                weights[index] += learning_rate * error * value
    if error_count == 0:
        break