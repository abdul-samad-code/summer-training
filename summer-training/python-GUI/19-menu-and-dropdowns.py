import tkinter as tk

root = tk.Tk()
root.title("Menu Bar Demo")
root.geometry("300x200")

def new_file():
    print("New file created")

def about():
    print("Tkinter Menu Demo v1.0")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exir", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
