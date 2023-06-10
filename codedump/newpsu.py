from tkinter import * 
from customtkinter import * 
import pandas as pd 
import numpy as np
import components as components 
import BCUTILS
from tkinter import messagebox
import sqlite3
'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''
def psu_window():
    dir="psu_png/"
    subwin=CTkToplevel()
    subwin.geometry=("700x700")
    subwin.configure(fg_color="#2E2E2E")

    title_label=CTkLabel(subwin, text= "Power Supply import", font=("Berlin", 40),text_color="#f37367")


    label_power= CTkLabel(subwin, text= "Power(W)", font=("Berlin", 20),text_color="#f37367")
    entry_power=CTkEntry(subwin, width=200, height=28, corner_radius=15,placeholder_text="e.g. 500", placeholder_text_color= "#f37367")
    label_newstock= CTkLabel(subwin, text= "New Units", font=("Berlin", 20),text_color="#f37367")
    entry_newstock=CTkEntry(subwin, width=200, height=28, corner_radius=15,placeholder_text="e.g. 1, 5", placeholder_text_color= "#f37367")

    title_label.grid(row=0, column=1, columnspan=2,padx=20,pady=20)
    label_power.grid(row=1, column=0)
    entry_power.grid(row=1, column=1)

    label_newstock.grid(row=2, column=0)
    entry_newstock.grid(row=2, column=1)

    def buttonpress():
        conn=sqlite3.connect("stock.db")
        c=conn.cursor()
        c.execute("UPDATE psu SET stock= stock+? WHERE power=?",(entry_newstock.get(), entry_power.get()))
        conn.commit()
        conn.close()
        entry_newstock.delete(0,END)
        entry_power.delete(0,END)
    def printbuttonpress():
        BCUTILS.getprintlist(dir,"requisites/psu_printlist.txt")
    button_psu=CTkButton(subwin, text="Submit",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b", corner_radius=15,command=buttonpress)
    button_psu.grid(row=3, column=1)
    printlist_button= CTkButton(subwin, text="Printlist",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b",corner_radius=15, command=printbuttonpress)
    printlist_button.grid(row=6, column= 2,columnspan=2,padx=20,pady=20)
    subwin.mainloop()
