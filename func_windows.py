from tkinter import * 
from tkinter import ttk
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


class in_windows:
    def GPU_CPU_window():
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


class view_windows:
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
            data.sort(key=lambda x: int(x[0]), reverse=reverse)
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
        
        
        def sort_column(tree, col, reverse):
            data = [(tree.set(child, col), child) for child in tree.get_children("")]
            data.sort(key=lambda x: int(x[0]), reverse=reverse)
            for index, (value, child) in enumerate(data):
                tree.move(child, "", index)
            tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

        headings= ("Brand","Name","Location", "ID")
        tree=ttk.Treeview(win,columns=headings, show='headings')
        tree.grid(row=1, column=0,pady=20)
        for heading in headings:
            tree.heading(heading, text=heading, command=lambda col=heading: sort_column(tree, col, False))
        
        for brand,name,location, id in zip(list_brand, list_name,list_loc, list_id):
            tree.insert('', 'end', values=(brand,name,location,id))
    
        
        win.mainloop()

    def psu_view():
        win=CTkToplevel()
        win.configure(fg_color="#2E2E2E")
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
        title_label=CTkLabel(win, text="PSU STOCK", font=("Berlin",20), text_color="#f37367")
        title_label.grid(row=0, column=0, padx=20, pady=20)
        def sort_column(tree, col, reverse):
            data = [(tree.set(child, col), child) for child in tree.get_children("")]
            data.sort(key=lambda x: int(x[0]), reverse=reverse)
            for index, (value, child) in enumerate(data):
                tree.move(child, "", index)
            tree.heading(col, command=lambda: sort_column(tree, col, not reverse))
        headings = ("Power", "Price", "Stock")
        tree = ttk.Treeview(win, columns=headings, show='headings')
        tree.grid(row=1, column=0)

        for heading in headings:
            tree.heading(heading, text=heading, command=lambda col=heading: sort_column(tree, col, False))
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

class adjustment_windows:
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
