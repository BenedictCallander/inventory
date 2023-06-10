from customtkinter import *
from tkinter import * 
from tkinter import ttk
import pandas as pd 
import datetime 

'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''

'''
other imports
'''
from backup import create_backup
from newimport import import_window
from prices_new import pricewindow

def main(): 
    win = CTk()
    win.geometry("960x540")
    win.configure(fg_color="#2E2E2E")
    win.title("Bedrock Inventory System 1.1")
    titleframe = CTkFrame(win)
    titleframe.configure(fg_color="#2E2E2E")
    titleframe.grid(row=0, column=0)
    icon = PhotoImage(file="requisites/icon.png")
    win.iconphoto(False,icon)
    titleimg = PhotoImage(file="requisites/bedrock.png")
    logotitle = Label(titleframe, image = titleimg,bg = "#2E2E2E")
    logotitle.grid(row=0, column= 0)
    titletext = Label(titleframe, text= "Bedrock Computers Inventory Management", font="Arial, 20", bg="#2E2E2E", fg="#de6210")
    titletext.grid(row=0, column= 1, columnspan= 1)
    buttonframe= CTkFrame(win)
    buttonframe.configure(fg_color="#2E2E2E")
    buttonframe.grid(row=1, column=0, pady=50)
    hvcol="#72c05b"
    button_fg = "#de6210"
    button1 = CTkButton(buttonframe, text="Add New Components", command=import_window,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200,corner_radius= 30) 

    button2 = CTkButton(buttonframe, text="Adjust Stock Price",command=pricewindow,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200,corner_radius= 30)
    
    button3 = CTkButton(buttonframe, text="Backup Database",command=create_backup,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b",height=100, width=200, corner_radius= 30)
    
    button4 = CTkButton(buttonframe, text="Alter Product Price",command=pricewindow,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 30)
    
    
    
    button5 = CTkButton(buttonframe, text="Button5",
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 30)

    button6 = CTkButton(buttonframe, text="Button6",
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 30) 

    button7 = CTkButton(buttonframe, text="Button7",
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 30) 
        
    button8 = CTkButton(buttonframe, text="Button8",
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 30) 
    
    button1.grid(row=4, column= 0,padx=15, pady=15)
    button2.grid(row=4, column=1,padx=15, pady=15)
    button3.grid(row=4, column=2,padx=15, pady=15)
    button4.grid(row=4, column=3,padx=15, pady=15)
    button5.grid(row=5, column=0,padx=15, pady=15)
    button6.grid(row=5, column=1,padx=15, pady=15)
    button7.grid(row=5, column=2,padx=15, pady=15)
    button8.grid(row=5, column=3,padx=15, pady=15)


    win.mainloop()

main()