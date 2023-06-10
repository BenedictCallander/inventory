import qrcode
from tkinter import * 
from customtkinter import *
import os
import uuid
class Product:
    def __init__(self, product_type, name, location):
        self.type = product_type
        self.name = name
        self.location= location
        self.prodid=uuid.uuid4()
        '''
        improve to implement automated location parsing
        '''
    def generate_qr_code(self):
        data = f'Type: {self.type}\nName: {self.name}'
        qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr_code.add_data(data)
        qr_code.make(fit=True)
        image = qr_code.make_image(fill_color="black", back_color="white")
        fname=f'temp_png/{self.type}_{self.name}.png'
        image.save(fname)
        return fname

def gen_save(type,name):
    instance=Product(type,name)
    fname=instance.generate_qr_code()
    return fname

def cleardir(dir):
    for filename in os.listdir(dir):
        file_path=os.path.join(dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
def getprintlist(directory, output_file):
    filenames = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            filenames.append(filename)

    with open(output_file, 'w') as file:
        file.write('\n'.join(filenames))

def codewindow():
    subwin= Toplevel()
    subwin.geometry("500x500")
    tempdir=r"temp_png/"
    cleardir(tempdir)
    
    label_title=Label(subwin, text="Generate QR code", font="Arial, 20")
    label_title.grid(row=0,column=0, columnspan= 4)
    label_type = Label(subwin, text="Product Type:", font="Arial, 20")
    label_type.grid(row=1, column= 1)
    label_name = Label(subwin, text="Product Name:", font="Arial, 20")
    label_name.grid(row=2, column= 1)

    entry_type=Entry(subwin); entry_type.grid(row=1, column= 2)
    entry_name= Entry(subwin); entry_name.grid(row=2, column= 2)

    def buttonpress():
        gen_save(str(entry_type.get()), str(entry_name.get()))
        entry_name.delete(0,END)
        entry_type.delete(0,END)
    def printbuttonpress():
        getprintlist(tempdir,"printlist.txt")


    submit_button= CTkButton(subwin, text="Submit", corner_radius=10,command=buttonpress)
    submit_button.grid(row=3, column= 1, columnspan=2)
    printlist_button= CTkButton(subwin, text="Printlist",corner_radius=10, command=printbuttonpress)
    printlist_button.grid(row=4, column= 1, columnspan=2)
    subwin.mainloop()
codewindow()