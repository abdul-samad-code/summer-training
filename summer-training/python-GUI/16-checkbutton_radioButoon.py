import tkinter as tk

root = tk.Tk()
root.title("Checkbutton and Radiobutton")

newsletter  = tk.BooleanVar()
tk.Checkbutton(root, text="Subscribe to newslatter", variable=newsletter).pack(anchor="w")

gender = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male",variable=gender, value="Male").pack(anchor="w")
tk.Radiobutton(root, text="Female", variable=gender, value="female").pack(anchor="w")


def show_value():
    print("Newsleter:", newsletter.get())
    print("Gender:", gender.get())

tk.Button(root, text="Submit", command=show_value,).pack(pady=10)

root.mainloop()