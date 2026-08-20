import tkinter as tk

root = tk.Tk()
root.title("Entry Widget")

name_var = tk.StringVar()

def show_name():
    print(f"Hello, {name_var.get()}")


tk.Label(root, text="Enter you rname").pack(pady=5)
tk.Entry(root, textvariable=name_var).pack(pady=5)
tk.Button(root, text="great", command=show_name).pack(pady=5)


root.mainloop()