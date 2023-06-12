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

class view_windows:
    def view_win():
        win=CTkToplevel()
        win.configure(fg_color="#2E2E2E")
        win.title("BEDROCK: COMPONENT STOCK VIEW")

        #
        # Set up frames and Grid
        #

        cpu_frame=CTkFrame(win, fg_color="#2E2E2E",border_color="black", border_width=2)
        psu_frame=CTkFrame(win, fg_color="#2E2E2E",border_color="black", border_width=2)
        psu_plot_frame=CTkFrame(win, fg_color="#2E2E2E",border_color="black", border_width=2)
        gpu_frame=CTkFrame(win, fg_color="#2E2E2E",border_color="black", border_width=2)
        ff_frame1=CTkFrame(win, fg_color="#2E2E2E",border_color="black", border_width=2)
        ff_frame2=CTkFrame(win, fg_color="#2E2E2E",border_color="black", border_width=2)

        cpu_frame.grid(row=1,column=0)
        ff_frame1.grid(row=1,column=1)
        psu_frame.grid(row=2, column=1)
        psu_plot_frame.grid(row=2, column=2)

        gpu_frame.grid(row=3, column=3)
        ff_frame2.grid(row=4,column=2)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="#2a2d2e",foreground="white",rowheight=25,fieldbackground="#343638",bordercolor="#343638",borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",background="#565b5e",foreground="white",relief="flat")
        style.map("Treeview.Heading",background=[('active', '#3484F0')])

        #
        #GPU
        #
        gpu_headings= ("Brand","Name","Location", "ID")
        gpu_title_label=CTkLabel(gpu_frame, text="GPU STOCK", font=("Berlin",20), text_color="#f37367")
        gpu_title_label.grid(row=0, column=0, padx=20, pady=20)
        #
        #read data
        #
        df_gpu= pd.read_csv("requisites/gpu.csv")
        gpu_list_brand= list(df_gpu['BRAND'])
        gpu_list_name=list(df_gpu['NAME'])
        gpu_list_loc=list(df_gpu['Location'])
        gpu_list_id=list(df_gpu['ID'])
        #
        #plot tree
        #
        gpu_headings = ("Brand", "Name", "Location", "ID")
        gpu_tree = ttk.Treeview(win, columns=gpu_headings, show='headings')
        gpu_tree.grid(row=1, column=0, padx=20, pady=20)
        for heading in gpu_headings:
            gpu_tree.heading(heading, text=heading)
        for brand, name, location, id in zip(gpu_list_brand, gpu_list_name,gpu_list_loc, gpu_list_id):
            gpu_tree.insert('', 'end', values=(brand, name, location, id))

        #
        #
        #

        #
        #CPU
        #
        
        df_cpu= pd.read_csv("requisites/cpu.csv")
        win.configure(fg_color="#2E2E2E")
        cpu_list_brand= list(df_cpu['BRAND'])
        cpu_list_name=list(df_cpu['NAME'])
        cpu_list_id=list(df_cpu['ID'])
        cpu_list_loc=list(df_cpu['Location'])

        cpu_title_label=CTkLabel(cpu_frame, text="CPU STOCK", font=("Berlin",20), text_color="#f37367")
        cpu_title_label.grid(row=0, column=0, padx=20, pady=20)

        cpu_headings= ("Brand","Name","Location", "ID")
        cpu_tree=ttk.Treeview(win,columns=cpu_headings, show='headings')
        cpu_tree.grid(row=1, column=0,pady=20)
        for heading in cpu_headings:
            cpu_tree.heading(heading, text=heading)
        
        for brand,name,location, id in zip(cpu_list_brand, cpu_list_name,cpu_list_loc, cpu_list_id):
            cpu_tree.insert('', 'end', values=(brand,name,location,id))

        #
        #
        #
        def sort_column(tree, col, reverse):
            data = [(tree.set(child, col), child) for child in tree.get_children("")]
            data.sort(key=lambda x: int(x[0]), reverse=reverse)
            for index, (value, child) in enumerate(data):
                tree.move(child, "", index)
            tree.heading(col, command=lambda: sort_column(tree, col, not reverse))
        
        #
        #psu_
        #
        conn=sqlite3.connect("requisites/stock.db")
        c = conn.cursor()
        c.execute('SELECT * from psu')
        datapsu = c.fetchall()
        psu_title_label=CTkLabel(psu_frame, text="PSU STOCK", font=("Berlin",20), text_color="#f37367")
        psu_title_label.grid(row=0, column=0, padx=20, pady=20)
        psu_headings = ("Power", "Price", "Stock")
        psu_tree = ttk.Treeview(psu_frame, columns=psu_headings, show='headings')
        psu_tree.grid(row=1, column=0,padx=20,pady=20)

        for heading in psu_headings:
            psu_tree.heading(heading, text=heading, command=lambda col=heading: sort_column(psu_tree, col, False))
        for i, (power, price, stock) in enumerate(datapsu):
            psu_tree.insert('', 'end', values=(power, price, stock))

            sum=0
        power,price,stock= zip(*datapsu)

        for i in range(len(power)):
            value=price[i]*stock[i]
            sum=sum+value
        total=CTkLabel(psu_frame,text=f'Total Value: £{sum}',font=("Berlin", 20),text_color="#f37367")
        total.grid(row=3, column=0,padx=20,pady=20)

        plot_title= CTkLabel(psu_plot_frame, text="PSU Stock History", text_color="#f37367", font=("Berlin", 30))
        plot_title.grid(row=0,column=0,padx=20,pady=20)
        fpath="requisites/temp_psu.png"
        plot_image=CTkImage(light_image=Image.open(fpath),size=(500,300))
        img_label=CTkLabel(psu_plot_frame, image=plot_image, text='')
        img_label.grid(row=1,column=0,padx=20,pady=20)

        conn.commit()
        conn.close()

        win.mainloop()





class view_windows:
    def gpu_view():
        win= CTkToplevel()
        win.title("BEDROCK: GPU STOCK INFO")
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
        
        headings = ("Brand", "Name", "Location", "ID")
        tree = ttk.Treeview(win, columns=headings, show='headings')
        tree.grid(row=1, column=0, padx=20, pady=20)
        for heading in headings:
            tree.heading(heading, text=heading)
        for brand, name, location, id in zip(list_brand, list_name, list_loc, list_id):
            tree.insert('', 'end', values=(brand, name, location, id))
        
        win.mainloop()
    
    def cpu_view():
        win= CTkToplevel()
        win.title("BEDROCK:CPU STOCK INFO")
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
        
        
        headings= ("Brand","Name","Location", "ID")
        tree=ttk.Treeview(win,columns=headings, show='headings')
        tree.grid(row=1, column=0,pady=20)
        for heading in headings:
            tree.heading(heading, text=heading)
        
        for brand,name,location, id in zip(list_brand, list_name,list_loc, list_id):
            tree.insert('', 'end', values=(brand,name,location,id))
    
        
        win.mainloop()

    def psu_view():
        win=CTkToplevel()
        win.title("BEDROCK:PSU STOCK INFO")
        win.configure(fg_color="#2E2E2E")
        chart_frame=CTkFrame(win, fg_color="#2E2E2E",border_color="black", border_width=2)
        chart_frame.grid(row=0,column=0,padx=20,pady=20)
        plot_frame=CTkFrame(win, fg_color="#2E2E2E",border_color="black", border_width=2)
        plot_frame.grid(row=0,column=1,padx=20,pady=20)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="#2a2d2e",foreground="white",rowheight=25,fieldbackground="#343638",bordercolor="#343638",borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",background="#565b5e",foreground="white",relief="flat")
        style.map("Treeview.Heading",background=[('active', '#3484F0')])
        conn = sqlite3.connect("requisites/stock.db")
        c = conn.cursor()
        c.execute('SELECT * from psu')
        datapsu = c.fetchall()
        title_label=CTkLabel(chart_frame, text="PSU STOCK", font=("Berlin",20), text_color="#f37367")
        title_label.grid(row=0, column=0, padx=20, pady=20)
        def sort_column(tree, col, reverse):
            data = [(tree.set(child, col), child) for child in tree.get_children("")]
            data.sort(key=lambda x: int(x[0]), reverse=reverse)
            for index, (value, child) in enumerate(data):
                tree.move(child, "", index)
            tree.heading(col, command=lambda: sort_column(tree, col, not reverse))
        headings = ("Power", "Price", "Stock")
        tree = ttk.Treeview(chart_frame, columns=headings, show='headings')
        tree.grid(row=1, column=0,padx=20,pady=20)

        for heading in headings:
            tree.heading(heading, text=heading, command=lambda col=heading: sort_column(tree, col, False))
        for i, (power, price, stock) in enumerate(datapsu):
            tree.insert('', 'end', values=(power, price, stock))

        sum=0
        power,price,stock= zip(*datapsu)
        
        for i in range(len(power)):
            value=price[i]*stock[i]
            sum=sum+value
        total=CTkLabel(chart_frame,text=f'Total Value: £{sum}',font=("Berlin", 20),text_color="#f37367")
        total.grid(row=3, column=0,padx=20,pady=20)

        plot_title= CTkLabel(plot_frame, text="PSU Stock History", text_color="#f37367", font=("Berlin", 30))
        plot_title.grid(row=0,column=0,padx=20,pady=20)
        fpath="requisites/temp_psu.png"
        plot_image=CTkImage(light_image=Image.open(fpath),size=(500,300))
        img_label=CTkLabel(plot_frame, image=plot_image, text='')
        img_label.grid(row=1,column=0,padx=20,pady=20)
        
        win.mainloop()