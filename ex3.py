from tkinter import *
import pandas as pd
 
# First window - Login page


def login():
    if username_entry.get() == "Divyaraj" and password_entry.get() == "vote":
        login_window.destroy()
        second_window()
        
       
login_window = Tk()
login_window.title("Login")
login_window.geometry("1920x1080")
 
welcome_label = Label(login_window, text="WELCOME TO e-VOTING", font=("Helvetica", 40))
welcome_label.pack(pady=100)
 
username_label = Label(login_window, text="Username:")
username_label.pack(pady=10)
username_entry = Entry(login_window ,width = 40 )
username_entry.pack()
 
password_label = Label(login_window, text="Password:")
password_label.pack(pady=10)
password_entry = Entry(login_window, show="*")
password_entry.pack()
 
login_button = Button(login_window, text="Login", command=login)
login_button.pack(pady=20)


 

 
# Second window - Registration page
def register():
    register_window = Toplevel()
    register_window.title("New Registration")
    register_window.geometry("1920x1080")
 
    name_label = Label(register_window, text="Name:")
    name_label.pack(pady=5)
    name_entry = Entry(register_window)
    name_entry.pack()
 
    surname_label = Label(register_window, text="Surname:")
    surname_label.pack(pady=5)
    surname_entry = Entry(register_window)
    surname_entry.pack()
 
    rfid_label = Label(register_window, text="RFID Card Number:")
    rfid_label.pack(pady=5)
    rfid_entry = Entry(register_window)
    rfid_entry.pack()
 
    mobile_label = Label(register_window, text="Mobile Number:")
    mobile_label.pack(pady=5)
    mobile_entry = Entry(register_window)
    mobile_entry.pack()
 
    city_label = Label(register_window, text="City:")
    city_label.pack(pady=5)
    city_entry = Entry(register_window)
    city_entry.pack()
 
    pincode_label = Label(register_window, text="Pincode:")
    pincode_label.pack(pady=5)
    pincode_entry = Entry(register_window)
    pincode_entry.pack()
 
    fingerprint_label = Label(register_window, text="Fingerprint:")
    fingerprint_label.pack(pady=5)
    fingerprint_entry = Entry(register_window)
    fingerprint_entry.pack()
 
    def submit():
        data = {"Name": [name_entry.get()],
                "Surname": [surname_entry.get()],
                "RFID Card Number": [rfid_entry.get()],
                "Mobile Number": [mobile_entry.get()],
                "City": [city_entry.get()],
                "Pincode": [pincode_entry.get()],
                "Fingerprint": [fingerprint_entry.get()]}
                
        #df = pd.read_csv("registration_details.csv")
        df = pd.DataFrame(data)
        df.to_csv("registration_details.csv", index=False)
        register_window.destroy()
 
    submit_button = Button(register_window, text="Submit", command=submit)
    submit_button.pack(pady=10)
 
def second_window():
    second_window = Tk()
    second_window.title("Second Window")
    second_window.geometry("1920x1080")
 
    new_registration_button = Button(second_window, text="New Registration", command=register)
    new_registration_button.pack(pady=10)
 
    vote_button = Button(second_window, text="Click Here to Vote")
    vote_button.pack(pady=10)
    second_window.mainloop()
 
second_window()


