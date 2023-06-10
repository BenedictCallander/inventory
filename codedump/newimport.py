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
def import_window():
    subwin=CTkToplevel()
    subwin.geometry=("700x700")
    subwin.configure(fg_color="#2E2E2E")
    dir="temp_png/"
    BCUTILS.cleardir(dir)

    label_title=CTkLabel(subwin, text="Add Stock", font=("Berlin", 20), text_color="#f37367")
    label_title.grid(row=0,column=0, columnspan= 4,padx=20,pady=20)
    label_type = CTkLabel(subwin, text="Product Type:", font=("Berlin", 20), text_color="#f37367")
    label_type.grid(row=1, column= 1,padx=20,pady=20)
    label_brand= CTkLabel(subwin, text="Brand", font=("Berlin", 20), text_color="#f37367")
    label_brand.grid(row=2, column= 1,padx=20,pady=20)
    label_name = CTkLabel(subwin, text="Product Name:", font=("Berlin", 20), text_color="#f37367")
    label_name.grid(row=3, column= 1,padx=20,pady=20)
    label_location= CTkLabel(subwin, text="Location", font=("Berlin", 20), text_color="#f37367")
    label_location.grid(row=4, column= 1,padx=20,pady=20)


    entry_type=CTkEntry(subwin, width=200)
    entry_brand=CTkEntry(subwin,width=200)
    entry_name= CTkEntry(subwin,width=200)
    entry_location= CTkEntry(subwin,width=200)
    
    entry_type.grid(row=1, column= 2,columnspan=3,padx=20,pady=20)
    entry_brand.grid(row=2, column= 2,columnspan=3,padx=20,pady=20)
    entry_name.grid(row=3, column= 2,columnspan=3,padx=20,pady=20)
    entry_location.grid(row=4, column=2,columnspan=3,padx=20,pady=20)
    
    def buttonpress():
        check= str(entry_type.get())
        if check == "CPU":
            addtask= components.cpu(entry_brand.get(), entry_name.get(), entry_location.get())
            addtask.add_gen()
            entry_type.delete(0,END)
            entry_brand.delete(0,END)
            entry_location.delete(0,END)
            entry_name.delete(0,END)

        elif check == "GPU":
            addtask= components.gpu(entry_brand.get(), entry_name.get(), entry_location.get())
            addtask.add_gen()
            conn=sqlite3.connect("requisites/stock.db")
            c=conn.cursor()
            c.execute("UPDATE gpu SET stock = stock + 1 WHERE name= ?",[addtask.name])
            conn.commit()
            conn.close()
            entry_type.delete(0,END)
            entry_brand.delete(0,END)
            entry_location.delete(0,END)
            entry_name.delete(0,END)
        else:
            messagebox.showerror("ERROR", "Invalid Type")
            entry_type.delete(0,END)
            entry_brand.delete(0,END)
            entry_location.delete(0,END)
            entry_name.delete(0,END)
        

    def printbuttonpress():
        BCUTILS.getprintlist(dir,"requisites/printlist.txt")

    submit_button= CTkButton(subwin, text="Submit",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b", corner_radius=15,command=buttonpress)
    submit_button.grid(row=5, column= 2, columnspan=2,padx=20,pady=20)
    printlist_button= CTkButton(subwin, text="Printlist",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b",corner_radius=15, command=printbuttonpress)
    printlist_button.grid(row=6, column= 2,columnspan=2,padx=20,pady=20)
    subwin.mainloop()


    
