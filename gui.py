'''
Created on Jul 23, 2021

@author: Matt Kennedy
'''

import tkinter as tk
from tkinter import ttk

"""
A class to create a view for a simple graphical calculator using Tkinter as
the parent class
"""
class Gui(tk.Tk):

    def __init__(self):
        
        # Initialize parent class
        super().__init__()
        self.title("PyCalculator")
        # Initialize graphical window
        self.create_gui()
        
    '''
    A function to call all sub functions needed to build the GUI
    '''
    def create_gui(self):
        self.create_main_frame()
        self.create_entry_element()
        self.create_button_elements()
    
    """
    A method to create the main graphical frame to hold all elements. 
    """
    def create_main_frame(self):
        pass
    
    def create_entry_element(self):
        pass
    
    def create_button_elements(self):
        pass
    
    '''
    Main function of class. Calls inherented mainloop method.
    NOTE: Calling this function starts an infinite loop.
    '''
    def main(self):
        self.mainloop()
 
 
if __name__ == "__main__":
    # Create Gui object
    gui = Gui()
    # Start the gui
    gui.main()       