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
    
    """
    A method to create calculator buttons.
    To do this, a series of rows of buttons ares created
    Since tk.pack defaults its orientation from top to bottom, individual buttons
    in each row must be packed to the left
    
    The calculator gui will consists of five rows of buttons in the following orientation
     C,+/-, /
     7, 8, 9, * 
     4, 5, 6, -
     3, 2, 1, +
     ., 0, = 
    
    """
    def create_button_elements(self):
        
        # Create an outer frame to fit the button frame. This will nest in the main frame
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()
        
        # Row 1:   C, +/-, /
        button_frame_row_1 = ttk.Frame(outer_frame)
        button_frame_row_1.pack()
        
        clear_button = ttk.Button(button_frame_row_1, text='C')
        clear_button.pack(side="left")
        
        inverse_button = ttk.Button(button_frame_row_1, text='+/-')
        inverse_button.pack(side="left")
        
        divide_button = ttk.Button(button_frame_row_1, text='/')
        divide_button.pack(side="left")
        
        button_frame_row_1.pack()
        
        # Row 2:  7, 8, 9, * 
        button_frame_row_2 = ttk.Frame(outer_frame)
        button_frame_row_2.pack()
        
        seven_button = ttk.Button(button_frame_row_2, text=7)
        seven_button.pack(side="left")
        
        eight_button = ttk.Button(button_frame_row_2, text=8)
        eight_button.pack(side="left")
        
        nine_button = ttk.Button(button_frame_row_2, text=9)
        nine_button.pack(side="left")
        
        mult_button = ttk.Button(button_frame_row_2, text='*')
        mult_button.pack(side="left")
        
        button_frame_row_2.pack()
        
        # Row 3:  4, 5, 6, -
        button_frame_row_3 = ttk.Frame(outer_frame)
        button_frame_row_3.pack()
        
        four_button = ttk.Button(button_frame_row_3, text=4)
        four_button.pack(side="left")
        
        five_button = ttk.Button(button_frame_row_3, text=5)
        five_button.pack(side="left")
        
        six_button = ttk.Button(button_frame_row_3, text=6)
        six_button.pack(side="left")
        
        sub_button = ttk.Button(button_frame_row_3, text='-')
        sub_button.pack(side="left")
        
        button_frame_row_3.pack()
        
        # Row 4 : 3, 2, 1, +
        button_frame_row_4 = ttk.Frame(outer_frame)
        button_frame_row_4.pack()
        
        three_button = ttk.Button(button_frame_row_4, text=3)
        three_button.pack(side="left")
        
        two_button = ttk.Button(button_frame_row_4, text=2)
        two_button.pack(side="left")
        
        one_button = ttk.Button(button_frame_row_4, text=1)
        one_button.pack(side="left")
        
        add_button = ttk.Button(button_frame_row_4, text='/')
        add_button.pack(side="left")
        
        button_frame_row_4.pack()
        
        # Row 5: ., 0, = 
        button_frame_row_5 = ttk.Frame(outer_frame)
        button_frame_row_5.pack()
        
        period_button = ttk.Button(button_frame_row_5, text='.')
        period_button.pack(side="left")
        
        zero_button = ttk.Button(button_frame_row_5, text=0)
        zero_button.pack(side="left")
        
        equals_button = ttk.Button(button_frame_row_5, text='=')
        equals_button.pack(side="left")
        
        button_frame_row_5.pack()
        
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