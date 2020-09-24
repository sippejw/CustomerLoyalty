from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
import re

root = Tk()
root.title('Chocolate Cellar Customer Loyalty')
root.geometry("400x400")

def submit():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    name_rex = re.compile("^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$")
    phone_rex = re.compile(
    if not name_rex.match(f_name.get()):
        messagebox.showerror("showerror","Invalid first name")
        return
    if not name_rex.match(l_name.get()):
        messagebox.showerror("showerror","Invalid last name")
        return

    c.execute("INSERT INTO customers (first_name, last_name, email_address, phone_number) VALUES (?, ?, ?, ?)", (f_name.get(), l_name.get(), email_address.get(), phone_number.get()))
    conn.commit()
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    phone_number.delete(0, END)
    email_address.delete(0, END)
    
# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
phone_number = Entry(root, width=30)
phone_number.grid(row=2, column=1)
email_address = Entry(root, width=30)
email_address.grid(row=3, column=1)

# Create labels
f_name_label = Label(root, text="First Name:")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name:")
l_name_label.grid(row=1, column=0)
phone_number_label = Label(root, text="Phone Number:")
phone_number_label.grid(row=2, column=0)
email_address_label = Label(root, text="Email:")
email_address_label.grid(row=3, column=0)

# Create submit button
submit_button = Button(root, text="Add Customer", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()
