from tkinter import *
from tkinter import ttk
from customtkinter import *
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import sqlite3
'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''

'''
conn = sqlite3.connect("stock.db")
    
c = conn.cursor()
c.execute('SELECT * from psu')
datapsu = c.fetchall()
    
c.execute ('SELECT * from gpu')
datagpu = c.fetchall()
    
c.execute("SELECT * from ram")
dataram = c.fetchall()
def gpu_view():
    win= Tk()
    win.geometry("500x500")
    #win.configure(fg_color="#2E2E2E")
    df_gpu= pd.read_csv("requisites/gpu.csv")
    labels=[]
    for i, (brand, name, price, stock) in enumerate(datagpu):
        txt_label_1 = CTkLabel(win, text="GPUs [brand, name, price]")#, text_color="#f37367", font=("monocraft", 20))
        txt_label_1.grid(row=0, column=0, padx=10,pady=10)
        gpu_brand_label = Label(win, text=brand)
        gpu_brand_label.grid(row=i+1, column=0)
        gpu_name_label = Label(win, text=name)
        gpu_name_label.grid(row=i+1, column=1)
        gpu_price_label = Label(win, text=price)
        gpu_price_label.grid(row=i+1, column=2)
        gpu_stock_label = Label(win, text=stock)
        gpu_stock_label.grid(row=i+1, column=3)
        labels.append(gpu_stock_label)
    win.mainloop()

gpu_view()

'''

class views:
    def gpu_view():
        win= CTkToplevel()
        win.configure(fg_color="#2E2E2E")
        df_gpu= pd.read_csv("requisites/gpu.csv")

        list_brand= list(df_gpu['BRAND'])
        list_name=list(df_gpu['NAME'])
        list_loc=list(df_gpu['Location'])
        list_id=list(df_gpu['ID'])
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="#2a2d2e",foreground="white",rowheight=25,fieldbackground="#343638",bordercolor="#343638",borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",background="#565b5e",foreground="white",relief="flat")
        style.map("Treeview.Heading",background=[('active', '#3484F0')])
        headings= ("Brand","Name","Location", "ID")
        title_label=CTkLabel(win, text="GPU STOCK", font=("Berlin",20), text_color="#f37367")
        title_label.grid(row=0, column=0, padx=20, pady=20)
        def sort_column(tree, col, reverse):
            data = [(tree.set(child, col), child) for child in tree.get_children("")]
            data.sort(reverse=reverse)
            for index, (value, child) in enumerate(data):
                tree.move(child, "", index)
            tree.heading(col, command=lambda: sort_column(tree, col, not reverse))
        headings = ("Brand", "Name", "Location", "ID")
        tree = ttk.Treeview(win, columns=headings, show='headings')
        tree.grid(row=1, column=0, padx=20, pady=20)
        for heading in headings:
            tree.heading(heading, text=heading, command=lambda col=heading: sort_column(tree, col, False))
        for brand, name, location, id in zip(list_brand, list_name, list_loc, list_id):
            tree.insert('', 'end', values=(brand, name, location, id))
        
        win.mainloop()
    def cpu_view():
        win= CTkToplevel()
        df_cpu= pd.read_csv("requisites/cpu.csv")
        win.configure(fg_color="#2E2E2E")
        list_brand= list(df_cpu['BRAND'])
        list_name=list(df_cpu['NAME'])
        list_id=list(df_cpu['ID'])
        list_loc=list(df_cpu['Location'])
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="#2a2d2e",foreground="white",rowheight=25,fieldbackground="#343638",bordercolor="#343638",borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",background="#565b5e",foreground="white",relief="flat")
        style.map("Treeview.Heading",background=[('active', '#3484F0')])
        title_label=CTkLabel(win, text="CPU STOCK", font=("Berlin",20), text_color="#f37367")
        title_label.grid(row=0, column=0, padx=20, pady=20)
        
        
        def sort_column_CPU(tree, col, reverse):
            data = [(tree.set(child, col), child) for child in tree.get_children("")]
            data.sort(reverse=reverse)
            for index, (value, child) in enumerate(data):
                tree.move(child, "", index)
            tree.heading(col, command=lambda: sort_column_CPU(tree, col, not reverse))

        headings= ("Brand","Name","Location", "ID")
        tree=ttk.Treeview(win,columns=headings, show='headings')
        tree.grid(row=1, column=0,pady=20)
        for heading in headings:
            tree.heading(heading, text=heading, command=lambda col=heading: sort_column_CPU(tree, col, False))
        
        for brand,name,location, id in zip(list_brand, list_name,list_loc, list_id):
            tree.insert('', 'end', values=(brand,name,location,id))
    
        
        win.mainloop()

    def view_psu():
        win=CTkToplevel()
        win.configure(fg_color="#2E2E2E")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="#2a2d2e",foreground="white",rowheight=25,fieldbackground="#343638",bordercolor="#343638",borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",background="#565b5e",foreground="white",relief="flat")
        style.map("Treeview.Heading",background=[('active', '#3484F0')])
        conn = sqlite3.connect("stock.db")
        c = conn.cursor()
        c.execute('SELECT * from psu')
        datapsu = c.fetchall()
        title_label=CTkLabel(win, text="PSU STOCK", font=("Berlin",20), text_color="#f37367")
        title_label.grid(row=0, column=0, padx=20, pady=20)
        def sort_column_PSU(tree, col, reverse):
            data = [(tree.set(child, col), child) for child in tree.get_children("")]
            data.sort(reverse=reverse)
            for index, (value, child) in enumerate(data):
                tree.move(child, "", index)
            tree.heading(col, command=lambda: sort_column_PSU(tree, col, not reverse))
        headings = ("Power", "Price", "Stock")
        tree = ttk.Treeview(win, columns=headings, show='headings')
        tree.grid(row=1, column=0)

        for heading in headings:
            tree.heading(heading, text=heading, command=lambda col=heading: sort_column_PSU(tree, col, False))
        for i, (power, price, stock) in enumerate(datapsu):
            tree.insert('', 'end', values=(power, price, stock))

        sum=0
        power,price,stock= zip(*datapsu)
        
        for i in range(len(power)):
            value=price[i]*stock[i]
            sum=sum+value
        total=CTkLabel(win,text=f'Total Value: £{sum}',font=("Berlin", 20),text_color="#f37367")
        total.grid(row=3, column=0)
        
        
        
        win.mainloop()
