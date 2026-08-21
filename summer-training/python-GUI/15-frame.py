import tkinter as tk

root = tk.Tk()
root.title("Frame and label Frame")


my_frame = tk.LabelFrame(root ,text="personl_details", padx=10, pady=10)
my_frame.pack(padx=10, pady=10, fill="x")

tk.Label(my_frame, text="Name:", ).grid(row=0, column=0, sticky="w")
tk.Entry(my_frame).grid(row=0, column=1, )

academic_frame = tk.LabelFrame(root, text="Academic details", padx=10, pady=10)
academic_frame.pack(padx=10, pady=10, fill="x")

tk.Label(academic_frame, text="Course:").grid(row=1, column=0, sticky="w")
tk.Entry(academic_frame).grid(row=1, column=1)

root.mainloop()
