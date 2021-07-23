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
        # Store the value of the operator
        self.operator = ''
        self.first_operand = ''
        # Keep track of whether or not the number being calculated is an int/float
        self.is_float = False
        # Keep track of whether or not an error was returned. This allows the error to be
        # displayed, while resetting state of the value to continue
        self.has_error = False
        
    """
    A function that receives an input (integer, operand, etc.) and determines
    what is needed for calculation 
    """
    def parse_input(self,input):
        # Check if an error exists. If it does, call the clear method
        if(self.has_error):
            self.clear()
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
            self.clear()
        
        # input is DEL
        elif(input == "DEL"):
            self.value = self.value[:-1]
            
        return self.value
    
    def clear(self):
        self.is_float = False
        self.first_operand = ''
        self.value = ''
        self.has_error = False
    def calculate(self, first_operand, operator, second_operand):
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
            self.has_error = True
            return "CANNOT DIVIDE BY ZERO"
        return float(x)/float(y)