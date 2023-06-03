from tkinter import *
import sqlite3
import pandas as pd
from datetime import datetime
conn = sqlite3.connect("stock.db")
    
c = conn.cursor()
c.execute('SELECT * from psu')
datapsu = c.fetchall()

c.execute ('SELECT * from gpu')
datagpu = c.fetchall()
   
c.execute("SELECT * from ram")
dataram = c.fetchall()

def viewram():
    data = dataram
    win=Toplevel()
    for i, (gen, capacity, stock) in enumerate(dataram):
        
