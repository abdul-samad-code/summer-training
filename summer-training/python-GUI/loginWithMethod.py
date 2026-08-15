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

    tk.Label(dashboard, text="Welcome to Dashboard").pack(pady=20)

root = tk.Tk()
root.withdraw()  # Hide root until login succeeds

login_window = tk.Toplevel(root)
login_window.title("Login")
login_window.geometry("300x200")

login_window.protocol("WM_DELETE_WINDOW", on_login_close)

tk.Label(login_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
user_entry = tk.Entry(login_window)
user_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
pass_entry = tk.Entry(login_window, show="*")
pass_entry.grid(row=1, column=1,padx=10, pady=10)

submit_button = tk.Button(login_window, text="Login", command=login)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

login_window.grab_set()
login_window.focus_force()

root.mainloop()