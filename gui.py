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
    main_frame is a class variable since other methods will need access
    to fill it
    """
    def create_main_frame(self):
        # Create instance of Frame from parent class
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack()
    
    """
    A method to create the entry element to hold the input/output data
    """
    def create_entry_element(self):
        entry = ttk.Entry(self.main_frame)
        entry.pack()
    
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