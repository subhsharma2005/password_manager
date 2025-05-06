from cryptography.fernet import Fernet #128 bit AES encryption 
import os
import tkinter as tk
from tkinter import messagebox

#creating or loading key
def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

fernet = load_key()

# add password
def add_password(site, password):
    encrypted_password = fernet.encrypt(password.encode())
    with open("passwords.txt", "a") as file:
        file.write(f"{site}:{encrypted_password.decode()}\n")

# get passwords
def get_password(site):
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            stored_site, encrypted_password = line.strip().split(":") #getting encrypted pass by spliting at ':'
            if stored_site == site:
                return fernet.decrypt(encrypted_password.encode()).decode()
    return None

# GUI 
def add_password_gui():
    site = site_entry.get() #take input in site_entry
    password = password_entry.get() #take input in password_entry
    if site and password:
        add_password(site, password) #input pass added
        messagebox.showinfo( "Password added",f"Password for {site} added.")
        site_entry.delete(0, tk.END) #removing data from variable used for input
        password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both site and password.")

def get_password_gui():
    site = site_entry.get()
    if site:
        password = get_password(site)
        if password:
            messagebox.showinfo("Password", f"Password for {site} is: {password}") 
        else:
            messagebox.showwarning("Not Found", f"No password found for {site}.")
        site_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter the site name.")

app = tk.Tk()
app.title("Password Manager")
app.configure(bg='#f0f0f0')
app.geometry("400x300")

header_frame = tk.Frame(app, bg='#4CAF50', height=50)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Password Manager", fg='white', bg='#4CAF50', font=('Arial', 16))
header_label.pack(pady=10)

content_frame = tk.Frame(app, bg='#f0f0f0')
content_frame.pack(fill=tk.BOTH, expand=True, pady=20, padx=20)

site_label = tk.Label(content_frame, text="Site:", bg='#f0f0f0', font=('Arial', 12))
site_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
site_entry = tk.Entry(content_frame, font=('Arial', 12))
site_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(content_frame, text="Password:", bg='#f0f0f0', font=('Arial', 12))
password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = tk.Entry(content_frame, show='*', font=('Arial', 12))
password_entry.grid(row=1, column=1, padx=10, pady=5)

button_frame = tk.Frame(content_frame, bg='#f0f0f0')
button_frame.grid(row=2, columnspan=2, pady=10)


add_button = tk.Button(button_frame, text="Add Password", command=add_password_gui, bg='#4CAF50', fg='white', font=('Arial', 12))
add_button.pack(side=tk.LEFT, padx=10)

get_button = tk.Button(button_frame, text="Get Password", command=get_password_gui, bg='#4CAF50', fg='white', font=('Arial', 12))
get_button.pack(side=tk.LEFT, padx=10)

#footer_label = tk.Label(app, text="Made by Subh Sharma", bg='#f0f0f0', font=('Arial', 10))
#footer_label.pack(side=tk.BOTTOM, pady=10)

app.mainloop()