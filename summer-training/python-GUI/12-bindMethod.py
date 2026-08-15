import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("return key pressed")

root = tk.Tk()

btn = ttk.Button(root, text="save" )
btn.bind('<return>', return_pressed)

btn.focus()
btn.pack(expand=True)


