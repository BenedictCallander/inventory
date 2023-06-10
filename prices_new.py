from customtkinter import *
from tkinter import * 
from tkinter import ttk
import uuid 
import csv
import sqlite3
import glob
import pandas as pd 
from pandastable import Table
from datetime import datetime
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''


def pricewindow():
    win=CTkToplevel()
    win.geometry=("1280x720")
    win.configure(fg_color="#2E2E2E")


    ramframe=CTkFrame(win)
    powerframe=CTkFrame(win)
    cpuframe=CTkFrame(win)
    gpuframe=CTkFrame(win)

    ramframe.grid(row=0, column=0,padx=20, pady=20); ramframe.configure(fg_color="#2E2E2E")
    powerframe.grid(row=0, column=1,padx=20, pady=20); powerframe.configure(fg_color="#2E2E2E")
    gpuframe.grid(row=0, column=2,padx=20, pady=20); gpuframe.configure(fg_color="#2E2E2E")
    
    
    '''
    ram ENTRIES
    '''

    title_ram= CTkLabel(ramframe, text= "RAM", text_color="#f37367", font=("Arial", 30))
    

    text_ram_generation = CTkLabel(ramframe, text="RAM GENERATION:", text_color="#f37367")
    entry_ram_generation=CTkEntry(ramframe, width=200, height=28, corner_radius=15,
    placeholder_text="GENERATION", placeholder_text_color= "#f37367")
    
    
    text_ram_capacity = CTkLabel(ramframe, text="RAM CAPACITY:", text_color="#f37367")
    entry_ram_capacity=CTkEntry(ramframe, width=200, height=28, corner_radius=15,
    placeholder_text="CAPACITY", placeholder_text_color= "#f37367")
    
    text_ram_cost= CTkLabel(ramframe, text="RAM COST:", text_color="#f37367")
    entry_ram_cost=CTkEntry(ramframe, width=200, height=28, corner_radius=15,
    placeholder_text="COST", placeholder_text_color= "#f37367")


    title_ram.grid(row=0, column=1,padx=20, pady=20)
    
    text_ram_generation.grid(row=1, column=0,padx=20, pady=20)
    text_ram_capacity.grid(row=2, column=0,padx=20, pady=20)

    entry_ram_generation.grid(row=1, column=1,padx=20, pady=20)
    entry_ram_capacity.grid(row=2, column=1,padx=20, pady=20)


    text_ram_cost.grid(row=3, column=0,padx=20, pady=20)
    entry_ram_cost.grid(row=3, column=1,padx=20, pady=20)

    def do_ram():
        conn= sqlite3.connect("requisites/stock.db")
        c=conn.cursor()
        c.execute("UPDATE ram SET price= ? WHERE gen=? AND capacity=?",
        (entry_ram_cost.get(), entry_ram_generation.get(),entry_ram_capacity.get()))
        conn.commit()
        conn.close()
        entry_ram_capacity.delete(0,END)
        entry_ram_cost.delete(0,END)
        entry_ram_generation.delete(0,END)
    

    button_ram= CTkButton(ramframe, width= 150, height=40, corner_radius=15, text= "Commit change", command= do_ram)
    button_ram.grid(row=4, column=0, columnspan=2,padx=20, pady=20)
    

    '''
    PSU Entries
    '''

    title_PSU = CTkLabel(powerframe, text="PSU", text_color="#f37367", font=("Arial", 30))


    text_PSU_power=CTkLabel(powerframe, text="PSU POWER", text_color="#f37367", font=("Arial", 20))
    text_PSU_price=CTkLabel(powerframe, text="PSU COST", text_color="#f37367", font=("Arial", 20))


    entry_PSU_power= CTkEntry(powerframe, width=200, height=28, corner_radius=15)
    entry_PSU_cost= CTkEntry(powerframe, width=200, height=28, corner_radius=15)

    title_PSU.grid(row=0, column=1,padx=20, pady=20)

    text_PSU_power.grid(row=1, column=0,padx=20, pady=20)
    text_PSU_price.grid(row=2, column=0,padx=20, pady=20)

    entry_PSU_power.grid(row=1, column=1,padx=20, pady=20)
    entry_PSU_cost.grid(row=2, column=1,padx=20, pady=20)
    def dopower():
        conn=sqlite3.connect("requisites/stock.db")
        c= conn.cursor()
        c.execute("UPDATE psu SET price=? WHERE power=?", (entry_PSU_cost.get(), entry_PSU_power.get()))
        conn.commit()
        conn.close()
        entry_PSU_cost.delete(0,END)
        entry_PSU_power.delete(0,END)

    button_power= CTkButton(powerframe, width= 150, height=40, corner_radius=15, text= "Commit change", command= dopower)
    button_power.grid(row=3, column=0, columnspan=2,padx=20, pady=20)

    '''
    GPU Entries
    '''

    title_GPU= CTkLabel(gpuframe, text= "GPU",text_color="#f37367", font=("Arial", 30) )

    text_GPU_brand= CTkLabel(gpuframe, text="BRAND", text_color="#f37367", font=("Arial", 20))
    text_GPU_name= CTkLabel(gpuframe, text= "NAME", text_color="#f37367", font=("Arial", 20))
    text_GPU_cost= CTkLabel(gpuframe, text="COST", text_color="#f37367", font=("Arial", 20))


    entry_GPU_brand=CTkEntry(gpuframe, width=200, height=28, corner_radius=15)
    entry_GPU_name=CTkEntry(gpuframe, width=200, height=28, corner_radius=15)
    entry_GPU_cost=CTkEntry(gpuframe, width=200, height=28, corner_radius=15)

    title_GPU.grid(row=0, column=1,padx=20, pady=20)
    text_GPU_brand.grid(row=1, column=0,padx=20, pady=20)
    text_GPU_name.grid(row=2, column=0,padx=20, pady=20)
    text_GPU_cost.grid(row=3, column=0,padx=20, pady=20)
    entry_GPU_brand.grid(row=1, column=1,padx=20, pady=20)
    entry_GPU_name.grid(row=2, column=1,padx=20, pady=20)
    entry_GPU_cost.grid(row=3, column=1,padx=20, pady=20)

    def do_gpu():
        conn=sqlite3.connect("requisites/stock.db")
        c=conn.cursor()
        c.execute("UPDATE gpu SET price=? WHERE brand=? AND name=? ",
        (entry_GPU_cost.get(),entry_GPU_brand.get(), entry_GPU_name.get())
        )
        conn.commit()
        conn.close()

        entry_GPU_brand.delete(0,END)
        entry_GPU_cost.delete(0,END)
        entry_GPU_name.delete(0,END)

    button_GPU = CTkButton(gpuframe, width= 150, height=40, corner_radius=15, text= "Commit change", command= do_gpu)
    button_GPU.grid(row=4, column=0, columnspan=2,padx=20, pady=20)
    win.mainloop()