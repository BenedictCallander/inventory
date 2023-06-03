import customtkinter as Ctk
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


def adjustwin():
    
    win= Toplevel()
    #win.config(bg="#2E2E2E")
    win.title("Bedrock Inventory System 1.1|         Stock Adjustments")
    icon = PhotoImage(file="icon.png")
    win.iconphoto(False,icon)
    
    conn = sqlite3.connect("stock.db")
    
    c = conn.cursor()
    c.execute('SELECT * from psu')
    datapsu = c.fetchall()
    
    c.execute ('SELECT * from gpu')
    datagpu = c.fetchall()
    
    c.execute("SELECT * from ram")
    dataram = c.fetchall()
    

    
    psu_labels = [] ; gpu_labels = []; ram_labels=[]
    psu_add_buttons = []; gpu_add_buttons= []; ram_add_buttons = []
    psu_remove_buttons = []; gpu_remove_buttons=[]; ram_remove_buttons=[]
    psu_frame = Frame(win); psu_frame.grid(row=0, column=0)
    gpu_frame = Frame(win); gpu_frame.grid(row=0, column= 1)
    ram_frame=Frame(win); ram_frame.grid(row=0, column= 2)
    for i, (power, stock) in enumerate(datapsu):
        power_label = Label(psu_frame, text=power)
        power_label.grid(row=i+1, column=0)
        title_label_1 = Label(psu_frame, text="PSU power (W)")
        title_label_1.grid(row=0, column= 0)
        stock_label = Label(psu_frame, text="Stock")
        stock_label.grid(row=0, column= 1)
        button_label=Label(psu_frame,text="Add/Remove")
        button_label.grid(row=0, column= 2, columnspan= 2)
        psu_stock_label = Label(psu_frame, text=stock)
        psu_stock_label.grid(row=i+1, column=1)
        psu_labels.append(psu_stock_label)
        psu_add_button = Button(psu_frame, text='+', command=lambda i=i: add_stock_psu(i))
        psu_add_button.grid(row=i+1, column=2)
        psu_add_buttons.append(psu_add_button)
        psu_remove_button = Button(psu_frame, text='-', command=lambda i=i: remove_stock_psu(i))
        psu_remove_button.grid(row=i+1, column=3)
        psu_remove_buttons.append(psu_remove_button)
    
    
    for i, (brand, name, price, stock) in enumerate(datagpu):
        
        title_label_1 = Label(gpu_frame, text="GPUs [brand, name, price]")
        title_label_1.grid(row=0, column= 0)
        stock_label = Label(gpu_frame, text="Stock")
        stock_label.grid(row=0, column= 3)
        button_label=Label(gpu_frame,text="Add/Remove")
        button_label.grid(row=0, column= 4, columnspan= 2)
        
        gpu_brand_label = Label(gpu_frame, text=brand)
        gpu_brand_label.grid(row=i+1, column=0)
        gpu_name_label = Label(gpu_frame, text=name)
        gpu_name_label.grid(row=i+1, column=1)
        gpu_price_label = Label(gpu_frame, text=price)
        gpu_price_label.grid(row=i+1, column=2)
        gpu_stock_label = Label(gpu_frame, text=stock)
        gpu_stock_label.grid(row=i+1, column=3)
        gpu_labels.append(gpu_stock_label)
        
        gpu_add_button = Button(gpu_frame, text='+', command=lambda i=i: add_stock_gpu(i))
        gpu_add_button.grid(row=i+1, column=4)
        gpu_add_buttons.append(gpu_add_button)
        gpu_remove_button = Button(gpu_frame, text='-', command=lambda i=i: remove_stock_gpu(i))
        gpu_remove_button.grid(row=i+1, column=5)
        gpu_remove_buttons.append(gpu_remove_button)
    
    for i, (gen, capacity, stock) in enumerate(dataram):
        
        title_label_1 = Label(ram_frame, text="Ram Generation")
        title_label_1.grid(row=0, column= 0)
        capacity_title=Label(ram_frame, text= "Capacity")
        capacity_title.grid(row=0, column= 1)
        stock_label = Label(ram_frame, text="Stock")
        stock_label.grid(row=0, column= 2)
        button_label=Label(ram_frame,text="Add/Remove")
        button_label.grid(row=0, column= 3, columnspan= 2)
        
        
        gen_label = Label(ram_frame, text=gen)
        gen_label.grid(row=i+1, column= 0)
        capacity_label = Label(ram_frame, text=capacity)
        capacity_label.grid(row=i+1,column= 1)
        ram_stock_label = Label(ram_frame, text=stock)
        ram_stock_label.grid(row=i+1, column= 2)
        ram_labels.append(ram_stock_label)
        
        ram_add_button = Button(ram_frame, text='+', command=lambda i=i: add_stock_ram(i))
        ram_add_button.grid(row=i+1, column=3)
        ram_add_buttons.append(ram_add_button)
        ram_remove_button = Button(ram_frame, text='-', command=lambda i=i: remove_stock_ram(i))
        ram_remove_button.grid(row=i+1, column=4)
        ram_remove_buttons.append(ram_remove_button)
        
        
        

    def add_stock_psu(i):
        c.execute('UPDATE psu SET stock = stock + 1 WHERE rowid = ?', (i+1,))
        conn.commit()
        # Update the stock label
        stock = c.execute('SELECT stock FROM psu WHERE rowid = ?', (i+1,)).fetchone()[0]
        psu_labels[i].config(text=stock)

    # Function to remove stock
    def remove_stock_psu(i):
        c.execute('UPDATE psu SET stock = stock - 1 WHERE rowid = ?', (i+1,))
        conn.commit()
        # Update the stock label
        stock = c.execute('SELECT stock FROM psu WHERE rowid = ?', (i+1,)).fetchone()[0]
        psu_labels[i].config(text=stock)
        
    def add_stock_gpu(i):
        c.execute('UPDATE gpu SET stock = stock + 1 WHERE rowid = ?', (i+1,))
        conn.commit()
        # Update the stock label
        stock = c.execute('SELECT stock FROM gpu WHERE rowid = ?', (i+1,)).fetchone()[0]
        gpu_labels[i].config(text=stock)

    # Function to remove stock
    def remove_stock_gpu(i):
        c.execute('UPDATE gpu SET stock = stock - 1 WHERE rowid = ?', (i+1,))
        conn.commit()
        # Update the stock label
        stock = c.execute('SELECT stock FROM gpu WHERE rowid = ?', (i+1,)).fetchone()[0]
        gpu_labels[i].config(text=stock)
    
    def add_stock_ram(i):
        c.execute('UPDATE ram SET stock = stock + 1 WHERE rowid = ?', (i+1,))
        conn.commit()
        # Update the stock label
        stock = c.execute('SELECT stock FROM ram WHERE rowid = ?', (i+1,)).fetchone()[0]
        ram_labels[i].config(text=stock)

    # Function to remove stock
    def remove_stock_ram(i):
        c.execute('UPDATE ram SET stock = stock - 1 WHERE rowid = ?', (i+1,))
        conn.commit()
        # Update the stock label
        stock = c.execute('SELECT stock FROM ram WHERE rowid = ?', (i+1,)).fetchone()[0]
        ram_labels[i].config(text=stock)
    
    
    
    win.mainloop()
    