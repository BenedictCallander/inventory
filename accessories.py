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
import uuid
'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''


class accessory:
    def __init__(self, type, brand, cost, location):
        self.type=type
        self.brand=brand
        self.cost=cost
        self.location=location
        self.acc_id=uuid.uuid4()
    def addto(self):
        df_add= pd.DataFrame({"Type":self.type, "Brand": self.brand, "cost": self.cost, "Location": self.location, "ID": self.acc_id},index=[0])
        dfin=pd.read_csv("requisites/accessories.csv")
        dflist=[dfin,df_add]
        df_output=pd.concat(dflist)
        df_output.to_csv("requisites/accessories.csv", index=False)

class acc_win:
    def accessorywindow():
        win=CTkToplevel()
        win.geometry("400x500")
        win.configure(fg_color="#2E2E2E")
        win.title("BEDROCK: ADD ACCESSORIES")
        text_title=CTkLabel(win, text="Add Accessory", font=("Berlin",40), text_color="#f37367")
        text_title.grid(row=0,column=0,padx=2,pady=2)
        inframe=CTkFrame(win, border_color="black",fg_color="#2E2E2E",border_width=2)
        inframe.grid(row=1,column=0,padx=20,pady=20)
        #Labels
        #
        text_Type=CTkLabel(inframe, text="Type:", font=("Berlin",15), text_color="#f37367")
        text_brand=CTkLabel(inframe, text="Brand", font=("Berlin",15), text_color="#f37367")
        text_cost=CTkLabel(inframe,text="Cost:", font=("Berlin",15), text_color="#f37367")
        text_location=CTkLabel(inframe,text="Location", font=("Berlin",15), text_color="#f37367")
        
        text_Type.grid(row=1,column=0,padx=20,pady=20)
        text_brand.grid(row=2, column=0,padx=20,pady=20)
        text_cost.grid(row=3, column=0,padx=20,pady=20)
        text_location.grid(row=4,column=0,padx=20,pady=20)


        entry_Type=CTkEntry(inframe, width=200)
        entry_brand=CTkEntry(inframe, width=200)
        entry_cost=CTkEntry(inframe, width=200)
        entry_location=CTkEntry(inframe, width=200)

        entry_Type.grid(row=1,column=1,padx=20,pady=20)
        entry_brand.grid(row=2, column=1,padx=20,pady=20)
        entry_cost.grid(row=3, column=1,padx=20,pady=20)
        entry_location.grid(row=4,column=1,padx=20,pady=20)

        def add_acc():
            obj=accessory(entry_Type.get(), entry_brand.get(), entry_cost.get(), entry_location.get())
            obj.addto()
            entry_Type.delete(0,END)
            entry_brand.delete(0,END)
            entry_cost.delete(0,END)
            entry_location.delete(0,END)
        
        add_button= CTkButton(inframe, text="Submit",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b", corner_radius=15,command=add_acc)
        add_button.grid(row=5, column=0, columnspan=2,padx=20,pady=20)
        win.mainloop()

