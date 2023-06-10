from tkinter import * 
from tkinter import ttk
from customtkinter import * 
import pandas as pd 
import numpy as np
import components as components 
import BCUTILS
from tkinter import messagebox
import sqlite3


class input_windows:
    def import_window():
        subwin=CTkToplevel()
        subwin=CTkToplevel()
        subwin.geometry=("700x700")
        subwin.configure(fg_color="#2E2E2E")
        cgpu_directory="temp_png/"
        psu_directory="psu_png/"
        gcpu_frame=CTkFrame(subwin)
        gcpu_frame.configure(fg_color="#2E2E2E")
        gcpu_frame.grid(row=1,column=0)
        BCUTILS.cleardir(cgpu_directory)
        label_title=CTkLabel(gcpu_frame, text="Add Stock", font=("Berlin", 20), text_color="#f37367")
        label_title.grid(row=0,column=0, columnspan= 4,padx=20,pady=20)
        label_type = CTkLabel(gcpu_frame, text="Product Type:", font=("Berlin", 20), text_color="#f37367")
        label_type.grid(row=1, column= 1,padx=20,pady=20)
        label_brand= CTkLabel(gcpu_frame, text="Brand", font=("Berlin", 20), text_color="#f37367")
        label_brand.grid(row=2, column= 1,padx=20,pady=20)
        label_name = CTkLabel(gcpu_frame, text="Product Name:", font=("Berlin", 20), text_color="#f37367")
        label_name.grid(row=3, column= 1,padx=20,pady=20)
        label_location= CTkLabel(gcpu_frame, text="Location", font=("Berlin", 20), text_color="#f37367")
        label_location.grid(row=4, column= 1,padx=20,pady=20)

        entry_type=CTkEntry(gcpu_frame, width=200)
        entry_brand=CTkEntry(gcpu_frame,width=200)
        entry_name= CTkEntry(gcpu_frame,width=200)
        entry_location= CTkEntry(gcpu_frame,width=200)
        
        entry_type.grid(row=1, column= 2,columnspan=3,padx=20,pady=20)
        entry_brand.grid(row=2, column= 2,columnspan=3,padx=20,pady=20)
        entry_name.grid(row=3, column= 2,columnspan=3,padx=20,pady=20)
        entry_location.grid(row=4, column=2,columnspan=3,padx=20,pady=20)
        
        def buttonpress_CGPU():
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
            

        def printbuttonpress_CGPU():
            BCUTILS.getprintlist(cgpu_directory,"requisites/printlist.txt")

        submit_button= CTkButton(gcpu_frame, text="Submit",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b", corner_radius=15,command=buttonpress_CGPU)
        submit_button.grid(row=5, column= 2, columnspan=2,padx=20,pady=20)
        printlist_button= CTkButton(gcpu_frame, text="Printlist",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b",corner_radius=15, command=printbuttonpress_CGPU)
        printlist_button.grid(row=6, column= 2,columnspan=2,padx=20,pady=20)

        power_frame=CTkFrame(subwin)
        power_frame.configure(fg_color="#2E2E2E")
        power_frame.grid(row=1, column=1)
        title_label=CTkLabel(power_frame, text= "Power Supply import", font=("Berlin", 40),text_color="#f37367")


        label_power= CTkLabel(power_frame, text= "Power(W)", font=("Berlin", 20),text_color="#f37367")
        entry_power=CTkEntry(power_frame, width=200, height=28, corner_radius=15,placeholder_text="e.g. 500", placeholder_text_color= "#f37367")
        label_newstock= CTkLabel(power_frame, text= "New Units", font=("Berlin", 20),text_color="#f37367")
        entry_newstock=CTkEntry(power_frame, width=200, height=28, corner_radius=15,placeholder_text="e.g. 1, 5", placeholder_text_color= "#f37367")

        title_label.grid(row=0, column=1, columnspan=2,padx=20,pady=20)
        label_power.grid(row=1, column=0)
        entry_power.grid(row=1, column=1)

        label_newstock.grid(row=2, column=0)
        entry_newstock.grid(row=2, column=1)

        def buttonpress_PSU():
            conn=sqlite3.connect("stock.db")
            c=conn.cursor()
            c.execute("UPDATE psu SET stock= stock+? WHERE power=?",(entry_newstock.get(), entry_power.get()))
            conn.commit()
            conn.close()
            entry_newstock.delete(0,END)
            entry_power.delete(0,END)
        def printbuttonpress_PSU():
            BCUTILS.getprintlist(psu_directory,"requisites/psu_printlist.txt")
        button_psu=CTkButton(power_frame, text="Submit",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b", corner_radius=15,command=buttonpress_PSU)
        button_psu.grid(row=3, column=1)
        printlist_button= CTkButton(power_frame, text="Printlist",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b",corner_radius=15, command=printbuttonpress_PSU)
        printlist_button.grid(row=4, column= 1,columnspan=2,padx=20,pady=20)
        
        
        subwin.mainloop()