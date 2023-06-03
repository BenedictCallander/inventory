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


def subwindow():
    win = Toplevel()
    win.geometry("1000x500")


    gpu_title=Label(win, text="GPU",font="Arial, 25")
    gpu_title.grid(row=0, column=0, padx=20, pady=20)

    #brand text, name text, price integer, stock integer
    gpu_brand_label=Label(win, text="GPU BRAND"); gpu_brand_label.grid(row=1, column= 1)
    #
    gpu_name_label=Label(win,text="Name"); gpu_name_label.grid(row=2, column= 1)
    #
    gpu_price_label = Label(win, text="Price"); gpu_price_label.grid(row=3,column =1)
    #
    gpu_stock_label=Label(win, text = "New Stock"); gpu_stock_label.grid(row=5, column=1)
    #
    gpu_brand_entry = Entry(win); gpu_name_entry = Entry(win); gpu_price_entry=Entry(win); gpu_stock_entry = Entry(win)
    gpu_brand_entry.grid(row=1,column=2); gpu_name_entry.grid(row=2, column= 2); gpu_price_entry.grid(row=3, column=2); gpu_stock_entry.grid(row=5, column=2)

    def collect_inputs_gpu_stock():
        conn=sqlite3.connect("stock.db")
        c=conn.cursor()
        c.execute("UPDATE gpu SET stock = stock+? where name=?", ( gpu_stock_entry.get(),gpu_name_entry()))
        conn.commit()
        conn.close()
        gpu_brand_entry.delete(0,END)
        gpu_name_entry.delete(0,END)
        gpu_price_entry.delete(0,END)
        gpu_stock_entry.delete(0,END)


    def collect_inputs_gpu_price():
        conn=sqlite3.connect("stock.db")
        c=conn.cursor()
        c.execute("UPDATE gpu SET price = ? where name=?", ( gpu_stock_entry.get(),gpu_name_entry()))
        conn.commit()
        conn.close()
        gpu_brand_entry.delete(0,END)
        gpu_name_entry.delete(0,END)
        gpu_price_entry.delete(0,END)
        gpu_stock_entry.delete(0,END)

    gpu_stockbutton = Button(win, text="Add item", command=collect_inputs_gpu_stock)
    gpu_stockbutton.grid(row=6, column= 2)
    gpu_pricebutton=Button(win, text="price change", command=collect_inputs_gpu_price)
    gpu_pricebutton.grid(row=4, column=2)

    ram_title=Label(win, text="RAM Inventory",font="Arial, 25"); ram_title.grid(row=0,column=5)

    gen_title=Label(win, text="Generation"); gen_title.grid(row=1, column= 5)

    capacity_title=Label(win, text="Capacity");capacity_title.grid(row=2, column= 5)

    schange_title = Label(win, text="Stock Change"); schange_title.grid(row=3, column= 5)

    gen_entry = Entry(win); cap_entry = Entry(win); schange_entry = Entry(win)

    gen_entry.grid(row=1, column= 6)
    cap_entry.grid(row=2, column= 6)
    schange_entry.grid(row=3, column= 6)

    def collect_inputs_ram():
        conn=sqlite3.connect("stock.db")
        c = conn.cursor()
        c.execute("UPDATE ram SET stock = stock+? WHERE gen = ? AND capacity=?",(schange_entry.get(),gen_entry.get(),cap_entry.get()))
        conn.commit()
        conn.close()
        schange_entry.delete(0,END)
        cap_entry.delete(0,END)
        gen_entry.delete(0,END)

    addbutton = Button(win,text='commit change', command=collect_inputs_ram)
    addbutton.grid(row=4, column= 6)

    blankfill=Label(win, text="     ")
    blankfill.grid(row=0, column= 7)

    psutitle=Label(win, text="PSU",font="Arial, 25")
    psutitle.grid(row=0, column= 8,padx=10)

    powertitle = Label(win, text="POWER:")
    powertitle.grid(row=1, column= 8,padx=10)

    quantitytitle=Label(win, text="Quantity")
    quantitytitle.grid(row=2, column=8,padx=10)

    powentry = Entry(win); powentry.grid(row=1, column=9)
    quantentry = Entry(win); quantentry.grid(row=2, column= 9)

    def collect_psu():
        conn = sqlite3.connect("stock.db")
        c=conn.cursor()
        c.execute("UPDATE psu quantity=quantity+? WHERE power =?", (quantentry.get(), powentry.get()))
        conn.commit()
        conn.close()

        quantentry.delete(0,END)
        powentry.delete(0,END)

    powerbutton=Button(win, text="ADD PSU STOCK", command=collect_psu)
    powerbutton.grid(row=4, column=9)