from customtkinter import *
from tkinter import * 
from tkinter import ttk
import pandas as pd 
import datetime 
from func_windows import in_windows, adjustment_windows, view_windows
from BCUTILS import backup
'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''

'''
other imports
'''

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
    titletext = Label(titleframe, text= "Bedrock Computers Inventory Management", font="Berlin, 20", bg="#2E2E2E", fg="#de6210")
    titletext.grid(row=0, column= 1, columnspan= 1)
    buttonframe= CTkFrame(win)
    buttonframe.configure(fg_color="#2E2E2E")
    buttonframe.grid(row=1, column=0, pady=50)
    hvcol="#72c05b"
    button_fg = "#de6210"


    button1 = CTkButton(buttonframe, text="Add New Components", command=in_windows.GPU_CPU_window,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200,corner_radius= 50) 

    button2 = CTkButton(buttonframe, text="Import PSU",command=in_windows.psu_window,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 50) 

    button3 = CTkButton(buttonframe, text="Adjust Stock Price",command=adjustment_windows.pricewindow,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200,corner_radius= 50)

    button4 = CTkButton(buttonframe, text="Button4",
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 50)

    button5 = CTkButton(buttonframe, text="View GPU's",command=view_windows.gpu_view,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 50)

    button6 = CTkButton(buttonframe, text="View CPU's",command=view_windows.cpu_view,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 50) 

    button7 = CTkButton(buttonframe, text="View PSU's",command=view_windows.psu_view,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b",height=100, width=200, corner_radius= 50)

    button8 = CTkButton(buttonframe, text="Backup Database",command=backup.create_backup,
    fg_color=button_fg,border_color="#72c05b",hover_color="#72c05b", height=100, width=200, corner_radius= 50) 
    
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