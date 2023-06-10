import sqlite3

connection = sqlite3.connect("stock.db")
cursor=connection.cursor()

cursor.execute("create table psu (power integer, price integer, stock integer)")


connection.close()