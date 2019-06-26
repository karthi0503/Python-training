# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 07:20:50 2019

@author: WELCOME
"""
#negative indexing
cars=[]

print(cars)

cars=['tata', 'skoda', 'maruti', 'mahindra', 'kia']

print(cars[-2])

#for loop

Students=['aaaa','bbbb','cccc']

for students in Students:
    print(students)
    
for studentss in Students:
    print(f"{studentss.title()}, practice daily")
    
    #working with number
    
num_value=list(range(1,10))
print(num_value)

for values in num_value:
    print(values)


squares=[]
for value in range(5,20):
    square=value**2
    squares.append(square)
    
print(squares)