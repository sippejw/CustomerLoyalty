import re

from tkinter import *
from tkinter import messagebox

from databaseInterface import incrementVisits, addCustomer

root = Tk()
root.title('Customer Loyalty')
root.geometry("400x400")

def main():
    root.mainloop()

def newSubmit():
    phone_rex = "^\(?([0-9]{3})\)?[-.]?([0-9]{3})[-.]?([0-9]{4})$"
    name_rex = "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$"
    email_rex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    
    if not re.match(name_rex, f_name.get()):
        messagebox.showerror("showerror","Invalid first name!")
        return
    if not re.match(name_rex, l_name.get()):
        messagebox.showerror("showerror","Invalid last name!")
        return
    if re.match(phone_rex, phone_number.get()):
        numbers = re.split(phone_rex, phone_number.get())
        numbers.remove("")
        phone_number_clean = "(" + numbers[0] + ")" + numbers[1] + "-" + numbers[2]
        print(phone_number_clean)
    else:
        messagebox.showerror("showerror","Invalid phone number!")
        return
    if not re.match(email_rex, email_address.get()):
        messagebox.showerror("showerror","Invalid email address!")
        return

    addCustomer(f_name.get(), l_name.get(), phone_number_clean, email_address.get())

    f_name.delete(0, END)
    l_name.delete(0, END)
    phone_number.delete(0, END)
    email_address.delete(0, END)

def returnSubmit():
    phone_rex = "^\(?([0-9]{3})\)?[-.]?([0-9]{3})[-.]?([0-9]{4})$"
    if re.match(phone_rex, customer_number.get()):
        numbers = re.split(phone_rex, customer_number.get())
        numbers.remove("")
        number_clean = "(" + numbers[0] + ")" + numbers[1] + "-" + numbers[2]
    else:
        messagebox.showerror("showerror", "Invalid phone number!")
        return
    num_visits = incrementVisits(number_clean)
    print(number_clean)
    print(num_visits)
    return
    
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
new_submit_button = Button(root, text="Add Customer", command=newSubmit)
new_submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

customer_number = Entry(root, width=30)
customer_number.grid(row=8, column=1)

customer_number_label = Label(root, text="Phone Number:")
customer_number_label.grid(row=8, column=0)

# Create submit button
returning_submit_button = Button(root, text="Add Visit", command=returnSubmit)
returning_submit_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



if __name__ == '__main__':
    main()
