import tkinter as tk

root = tk.Tk()
root.title("Scale and Spinbox")

volume = tk.Scale(root , from_=0, to=100, orient="horizontal", label="volume")
volume.set(70)
volume.pack(padx=10, pady=10, fill="x")

age_spin = tk.Spinbox(root, from_=18, to=60, )
age_spin.pack(padx=10, pady=10, fill="x")

def show_values():
    print("Volume.:", volume.get())
    print("Age:", age_spin.get())

tk.Button(root, text="Show Values", command=show_values).pack()

root.mainloop()
