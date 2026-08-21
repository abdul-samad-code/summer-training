import tkinter as tk
root = tk.Tk()
root.title("Control Variables")

name = tk.StringVar(value="Aman")
age = tk.IntVar(value=20)
gpa = tk.DoubleVar(value=8.5)
is_hostler  =tk.BooleanVar(value=True)

tk.Label(root, textvariable=name).pack()  # stays in sync with `name automatically

def increase_age():
    age.set(age.get()+1)

tk.Button(root, text="Birthday!", command=increase_age).pack()

print(f"Name: {name.get()}, age: {age.get()}, GPA: {gpa.get()}, Hostler: {is_hostler.get()}")

root.mainloop()

