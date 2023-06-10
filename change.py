power_frame=1


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
        button_psu=CTkButton(power_frame, text="Submit",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b", corner_radius=15,command=buttonpress)
        button_psu.grid(row=3, column=1)
        printlist_button= CTkButton(power_frame, text="Printlist",width=250, height=100, fg_color="#f37367", hover_color= "#72c05b",corner_radius=15, command=printbuttonpress)
        printlist_button.grid(row=6, column= 2,columnspan=2,padx=20,pady=20)
        power_frame.mainloop()