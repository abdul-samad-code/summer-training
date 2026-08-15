import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def button_clicked():
    print("button clicked")

button = ttk.Button(root, text="click me", command=button_clicked)
button.pack()
root.mainloop()