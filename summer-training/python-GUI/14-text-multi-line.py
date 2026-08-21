import tkinter as tk

root = tk.Tk()
root.title("text widget")

text_box = tk.Text(root, height=5, width=30)
text_box.pack(padx=10, pady=10)
text_box.insert("1.8", "heey samad")

content =text_box.get("1.0", "end-1c")
print("content:", content)

root.mainloop()
                