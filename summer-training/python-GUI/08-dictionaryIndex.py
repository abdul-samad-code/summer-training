import tkinter as tk
from tkinter import ttk

root = tk.Tk()
label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()

root.mainloop()