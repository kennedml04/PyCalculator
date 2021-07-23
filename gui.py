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

    def __init__(self, params):
        '''
        Constructor
        '''
        