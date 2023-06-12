from tkinter import * 
from customtkinter import * 
import sqlite3
import pandas as pd 
import uuid

'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''

class used_sys:
    def __init__(self, Manufactuer, cpu, storage, power, location):
        self.manufac=Manufactuer
        self.cpu=cpu
        self.storage=storage
        self.power=power
        self.loc=location
        self.sys_ID=uuid.uuid4()
        

    def add_stock(self):
        
        data_system=pd.DataFrame({"Manufacturer":self.manufac,
                                   "CPU": self.cpu,
                                     "RAM": self.storage,
                                       "PSU": self.power,
                                         "Location":self.loc,
                                           "ID":self.sys_ID},index=[0])
        df_input=pd.read_csv("requisites/systems.csv")
        dflist=[df_input, data_system]
        df_output=pd.concat(dflist)
        df_output.to_csv("requisites/systems.csv", index=False)


class used_window():
    def used_win():
        win=CTkToplevel()
        win.geometry("900x500")
        win.configure(fg_color="#2E2E2E")
        text_label=CTkLabel(win, text="Used System Import",font=("Berlin",50), text_color="#f37367")
        text_label.grid(row=0,column=0,columnspan=2)

        inputframe=CTkFrame(win,border_color="#72c05b",border_width=3)
        inputframe.grid(row=1,column=0)
        inputframe.configure(width=400, height=400,fg_color="#2E2E2E")
        buttonframe=CTkFrame(win, border_color="#72c05b",border_width=3)
        buttonframe.grid(row=1,column=1, padx=20)
        buttonframe.configure(width=400, height=400,fg_color="#2E2E2E")
        
        labels=["Manufacturer", "Processor", "RAM", "PSU", "Location"]
        i=0       
        for label in labels:
            text=CTkLabel(inputframe, text=label, font=("Berlin",20), text_color="#f37367")
            text.grid(row=i+1, column=0,padx=20, pady=20)
            i=i+1
        
        entry_man=CTkEntry(inputframe, width=200)
        entry_man.grid(row=1, column=1,padx=20, pady=20)
        entry_processor=CTkEntry(inputframe, width=200)
        entry_processor.grid(row=2, column=1,padx=20, pady=20)
        entry_ram=CTkEntry(inputframe, width=200)
        entry_ram.grid(row=3, column=1,padx=20, pady=20)
        entry_power=CTkEntry(inputframe, width=200)
        entry_power.grid(row=4, column=1,padx=20, pady=20)
        entry_location=CTkEntry(inputframe, width=200)
        entry_location.grid(row=5, column=1,padx=20, pady=20)

        def add_system():
            system=used_sys(entry_man.get(), entry_processor.get(), entry_ram.get(), entry_power.get(), entry_location.get())
            system.add_stock()
            entry_location.delete(0,END)
            entry_man.delete(0,END)
            entry_power.delete(0,END)
            entry_processor.delete(0,END)
            entry_ram.delete(0,END)
        
        addbutton=CTkButton(buttonframe,text="Submit",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b", corner_radius=15,command=add_system)
        addbutton.pack(padx=20,pady=20)
        win.mainloop()
