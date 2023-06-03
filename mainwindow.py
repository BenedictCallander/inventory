from customtkinter import *
from tkinter import * 
from tkinter import ttk
import pandas as pd 

import datetime 

'''
other imports
'''
from adjustments import adjustwin
from backup import create_backup
from components import subwindow
def main(): 
    win = Tk()
    win.geometry("1280x720")
    win.title("Bedrock Inventory System 1.1")
    icon = PhotoImage(file="icon.png")
    win.iconphoto(False,icon)
    win.configure(bg="#2E2E2E")
    titleimg = PhotoImage(file="bedrock.png")
    logotitle = Label(win, image = titleimg,bg = "#2E2E2E")
    logotitle.grid(row=0, column= 0)
    titletext = Label(win, text= "Bedrock Computers", font="Arial, 20", bg="#2E2E2E", fg="#de6210")
    titletext2 = Label(win, text= "Inventory Management", font="Arial, 20", bg="#2E2E2E", fg="#de6210")
    titletext.grid(row=1, column= 0, columnspan= 1)
    titletext2.grid(row=2, column= 0, columnspan= 1)
    button_bg = "#2E2E2E"
    button_fg = "#de6210"
    button1 = Button(win, text="Add New Components",command=subwindow, bg=button_bg, fg=button_fg, height=5, width=20); button1.grid(row=4, column= 1)
    button2 = Button(win, text="Adjust Stock Properties",command=adjustwin, bg=button_bg, fg=button_fg, height=5, width=20); button2.grid(row=4, column=2)
    button3 = Button(win, text="Button3", bg=button_bg, fg=button_fg, height=5, width=20); button3.grid(row=4, column=3)
    button4 = Button(win, text="Manual Backup",command=create_backup, bg=button_bg, fg=button_fg, height=5, width=20); button4.grid(row=4, column=4)
    button5 = Button(win, text="Button5",bg=button_bg, fg=button_fg, height=5, width=20); button5.grid(row=5, column=1)
    button6 = Button(win, text="Button6",bg=button_bg, fg=button_fg, height=5, width=20); button6.grid(row=5, column=2)
    button7 = Button(win, text="Button7",bg=button_bg, fg=button_fg, height=5, width=20); button7.grid(row=5, column=3)
    button8 = Button(win, text="Button8",bg=button_bg, fg=button_fg, height=5, width=20); button8.grid(row=5, column=4)
    
   
    win.mainloop()

main()