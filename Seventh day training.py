# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 07:20:11 2019

@author: WELCOME
"""

#tuple
radiusvalue=(25,65)

print(radiusvalue[0])

radiusvalue=(25,35,45)

print("original values")

for values in radiusvalue:
    print(values)
    
    radiusvalue=(55,65,75)

print("\nmodified values")

for values in radiusvalue:
    print(values)
    
#if statement

languages=['java','python','c#','sql']

for language in languages:
    if language =='sql':
        print(language.upper())
    else:
        print(language.title())
        
#python is case sensitive

language= 'SQL'
languages = 'sql'

if language == languages:
    print("success")
else:
    print("case sensitive")
    
language= 'SQL'
languages = 'sql'

if language != languages:
    print("yes! python is case sensitive")
else:
    print("not a case sensitive")