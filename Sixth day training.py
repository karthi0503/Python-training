# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 07:16:28 2019

@author: WELCOME
"""

#slicing of Lists

companies=['CTS','Infy','Cognizant','Syntel','Hexaware']

print(companies[0:4])

print(companies[1:])

print(companies[:5])

print('first 4 companies i worked')

for company in companies[:4]:
    print(company)
    
#copying the lists
companies_name = companies[:]
print(companies)

companies.append('Virtusa')

companies_name.append('Virtusa Polaris')

print(companies)

print(companies_name)