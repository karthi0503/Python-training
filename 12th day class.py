# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 07:44:06 2019

@author: WELCOME
"""

#WHile Loops

n=12    
i=1

sum=0

num_value=list(range(i,n))

while i <=n :
    sum = sum+i
    i=i+1
print(f"the answer is,{sum}")    


# while loop with else

n=int(input("PLease eneter a value to sum") )
i=1

sum=0

num_value=list(range(i,n))

while i <=n :
    sum = sum+i
    i=i+1
    print(f"the answer is,{sum}")    
else:
    print(f"The value {i} is greater than input {n}")