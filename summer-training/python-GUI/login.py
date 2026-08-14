import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Login Form")
root.geometry("400x300")

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        showinfo("Login", "Login Successful!")
    else:
        showinfo("Login", "Invalid Username or Password")


# Heading
ttk.Label(
    root,
    text="Login Form",
    font=("Arial", 20, "bold")
).pack(pady=20)

# Username
ttk.Label(root, text="Username").pack()

username_entry = ttk.Entry(root, width=30)
username_entry.pack(pady=5)

# Password
ttk.Label(root, text="Password").pack()

password_entry = ttk.Entry(
    root,
    width=30,
    show="*"
)
password_entry.pack(pady=5)

# Login Button
ttk.Button(
    root,
    text="Login",
    command=login
).pack(pady=20)

root.mainloop()