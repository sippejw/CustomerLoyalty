from tkinter import *

from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Chocolate Cellar Customer Loyalty')
root.geometry("400x400")

conn = sqlite3.connect('database.db')

c = conn.cursor()

def submit():
    if f_name == '':
        print('test')

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

conn.commit()
conn.close()
root.mainloop()
