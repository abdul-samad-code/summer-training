import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def login():
    userName = user_entry.get()
    password = pass_entry.get()

    if userName == "admin" and password == "123":
        login_window.destroy()   # close login window
        show_dashboard() 
    else:
        messagebox.showerror("Error", "Invalid credentials")
def  on_login_close():
    root.destroy() # close entire applicaton

def show_dashboard():
    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")