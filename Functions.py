# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:12:49 2019

@author: WELCOME
"""

#functions

def first_fun():
    """This function ius to display the given input name with the text given inside string f"""
    a=input("enter a name to disply with a text")
    print(f"{a} writes the first function in Python" )
    print(first_fun.__doc__)
   
    
#function with Parameters

def parameterized_fun(name,language):
    """This function ius to display the given input name with the text given inside string f"""
    
      
    print(f"{name} writes the first function in {language}" )
    
 
    
#function to pass a  Parameter with default value    

def parameter_default_fun(name,language='Python'):
    """This function ius to display the given input name with the text given inside string f"""
    
      
    print(f"{name} writes the first function in {language}" )
    

    
# function to return the ouytput as dictionary format:
    
    

    
def parameter_dict_fun(d_name,d_language):
    """This function is to display the given input name with the text given inside string"""
    input_dict = {'display_name': d_name, 'display_lang': d_language}

    return input_dict

inputs_par=parameter_dict_fun('Karthikeyan','Python')
      
print(inputs_par)
    


#for loop and arbitrary in functions

def parameter_forarb_fun(*days):
    for daays in days:
        print(f"Hello {daays} ")  



    