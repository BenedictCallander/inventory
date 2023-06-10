from tkinter import * 
from customtkinter import * 


def main():
    win= Tk()
    win.geometry("1280x720")
    win.title("Bedrock2")

    def buttonpress():
        print("button")
    
    text1=Label(win, text="test")
    text1.grid(row=1, column= 1)

    button1=CTkButton(win, corner_radius=10, command=buttonpress)
    button1.grid(row=2, column=2)

    win.mainloop()
main()