from tkinter import * 
from tkinter import ttk
from customtkinter import * 
import pandas as pd 
import numpy as np
import components as components 
import BCUTILS
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''



'''
Get ORDERS Psuedocode


press get orders button-> connect to API 
obtain all orders-> disect into individual components

if ? =? search ? -> return location and ID 
collect for all: summarise into single display -> print? 
scan individual barcode-> remove item from stock 

'''

def get_orders():
    subwin=CTkToplevel()
    subwin.geometry("200x200")
    subwin.configure(fg_color="#2E2E2E")
    label=CTkLabel(subwin, text="INDEV", font=("Berlin",30),text_color="#f37367")
    label.pack()
    
    subwin.mainloop()
