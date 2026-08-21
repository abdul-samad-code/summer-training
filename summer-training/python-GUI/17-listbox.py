import tkinter as tk

root = tk.Tk()
root.title("Listbox")

subjects = tk.Listbox(root, selectmode="multiple")
for subject in ["Ai", "dev", "dsa", "network"]:
    subjects.insert("end", subject)
subjects.pack(padx=10, pady=10)

def show_selection():
    selected = [subjects.get(i) for i in subjects.curselection()]
    print("Selected:", selected)

tk.Button(root,  text="Show Selection", command=show_selection).pack()

root.mainloop()