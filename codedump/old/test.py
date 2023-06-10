from tkinter import ttk
from tkinter import *
'''
def sort_column(tree, col, reverse):
    data = [(tree.set(child, col), child) for child in tree.get_children("")]
    data.sort(reverse=reverse)
    for index, (value, child) in enumerate(data):
        tree.move(child, "", index)
    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

headings = ("Power", "Price", "Stock")
win = Tk()

tree = ttk.Treeview(win, columns=headings, show='headings')
tree.grid(row=1, column=0)

for heading in headings:
    tree.heading(heading, text=heading, command=lambda col=heading: sort_column(tree, col, False))

datapsu = [("Power1", "Price1", "Stock1"), ("Power2", "Price2", "Stock2"), ("Power3", "Price3", "Stock3")]

for i, (power, price, stock) in enumerate(datapsu):
    tree.insert('', 'end', values=(power, price, stock))

win.mainloop()
'''