'''
Created on Jul 23, 2021

@author: Matt Kennedy
'''

"""
A class to parse input from the user and return output to the GUI 
"""
class Calculator:

    def __init__(self):
        self.value = ''
        
    """
    A function that receives an input (integer, operand, etc.) and determines
    what is needed for calculation 
    """
    def parse_input(self,input):
        # input is a number
        if(isinstance(input,int)):
            self.value += str(input)
            #print(f'{input} was input')
        # input is a decimal point
        
        # input is an operator
        
        # input is equal sign
        
        # input is inverse
        
        # input is clear
        return self.value