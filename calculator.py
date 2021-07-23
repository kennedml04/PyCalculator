'''
Created on Jul 23, 2021

@author: Matt Kennedy
'''
from pickle import FALSE

"""
A class to parse input from the user and return output to the GUI 
"""
class Calculator:

    def __init__(self):
        self.value = ''
        self.operator = ''
        self.first_operand = ''
        self.is_float = False
        
    """
    A function that receives an input (integer, operand, etc.) and determines
    what is needed for calculation 
    """
    def parse_input(self,input):
        # input is a number
        if(isinstance(input,int)):
            self.value += str(input)
        # input is a decimal point
        elif(input=="."):
            self.value += input
            self.is_float = True
        # input is an operator
        elif(input == '/' or input== '*' or input== '+' or input == '-'):
            # save first_operand
            self.first_operand = self.value
            # save operator
            self.operator = input
            # clear value for second operand
            self.value = ''
             
        # input is equal sign
        elif(input == "="):
            self.calculate(self.first_operand,self.operator,self.value)
        # input is inverse
        elif(input == "+/-"):
            if self.value[0] == '-':
                self.value = self.value[1:]
            else:
                self.value = '-' + self.value
            
        # input is clear
        elif(input == 'C'):
            self.is_float = False
            self.first_operand = ''
            self.value = ''
            
        return self.value
    
    def calculate(self, first_operand, operator, second_operand):
        print("IN CALCULATE")
        if operator == "+":
            if(self.is_float):
                self.value = self.add_float(first_operand, second_operand)
            else:
                self.value = self.add_int(first_operand, second_operand)
        elif operator == "-":
            if(self.is_float):
                self.value = self.subtract_float(first_operand,second_operand)
            else:
                self.value = self.subtract_int(first_operand,second_operand)
        elif operator == "/":
                self.value = self.divide(first_operand, second_operand)
        elif operator == "*":
            if(self.is_float):
                self.value = self.multiply_float(first_operand, second_operand)
            else:
                self.value = self.multiply_int(first_operand, second_operand)
                
    def add_int(self, x,y):
        return int(x)+int(y)
    
    def add_float(self, x,y):
        return float(x)+float(y)
    
    def subtract_int(self,x,y):
        return int(x)-int(y)
    
    def subtract_float(self,x,y):
        return float(x)-float(y)

    def multiply_int(self,x,y):
        return int(x)*int(y)

    def multiply_float(self,x,y):
        return float(x)*float(y)
    
    def divide(self,x,y):
        if(int(y) == 0):
            return "CANNOT DIVIDE BY ZERO"
        return float(x)/float(y)
   