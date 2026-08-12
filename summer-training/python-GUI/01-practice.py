import tkinter as tk
from tkinter import ttk

root = tk.Tk()
def newWindow():
    newWindow = tk.Toplevel(root)
    newWindow.title("new window")
    newWindow.geometry("700x400")
    tk.Label(root, text="this is new window").pack()
    ttk.Button(newWindow, text="close", command=newWindow).pack()

tk.Label(root,
          text="classic label", font=("Arial", 20, "bold italic",), fg="red").pack()
ttk.Label(root, text="themed label").pack()
"""
buttonName = ttk.Button(
root,
master,
text="text"),
command=callback
"""
button = tk.Button(root, text="classic button",).pack()
button2 = ttk.Button(root, text="themed button",
                    command=lambda: print("themed button clicked")).pack()

button3 = ttk.Button(root, text="open new window",
 command=newWindow).pack()
root.mainloop()