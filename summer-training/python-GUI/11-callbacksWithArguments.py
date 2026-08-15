import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def select(option):
    print(option)

ttk.Button(root, text="rock", command=lambda: select('rock')).pack()
ttk.Button(root, text="paper", command=lambda: select('paper')).pack()
ttk.Button(root, text="scissors", command=lambda: select('scissors')).pack()


root.mainloop()