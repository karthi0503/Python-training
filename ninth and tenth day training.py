# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 08:18:52 2019

@author: WELCOME
"""

#dictionaries

dictions={'name':'Karthikeyan','id':613}

print(dictions['name'])
print(dictions['id'])

fontcolor={'color':'Yellow'}
print(f"the font is displayed in {fontcolor['color']}.")

fontcolor={'color':'Orange'}
print(f"the font color changed to {fontcolor['color']}.")

fontvalues={'color':'Orange','size':12,'font':'Calibri','command':'delete this point using delete function'}
print(fontvalues)
del fontvalues['command']
print(fontvalues)

fontupdate=fontvalues.get('command','the command key is deleted hence insert the key and print or try another key')
print(fontupdate)

fontfont={'font':'calibri','font1':'time new ','font2':'Calibri','font3':'Calibri','font4':'Calibri','font5':'Calibri'}
print(fontfont['font'].title())

print("\nLooping through the dictionary Values")
for key,value in fontfont.items():
    print(f"\nKey :{key}")
    print(f"Value :{value}")
    exit
    
print("\nPrint Keys")
for key in fontfont.keys():
    print(f"\nKey :{key}")
exit
print("\nPrint Values")
for value in fontfont.values():
    print(f"\nKey :{value}")


print("Insert values to the dictionary")
fontvalues.update({'bold':'true'})
print("\nthe updated fontvalues" )
print(fontvalues)