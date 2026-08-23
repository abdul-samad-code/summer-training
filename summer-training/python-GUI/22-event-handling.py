import tkinter as tk

root = tk.Tk()
root.title("Event Binding")
root.geometry("300x200")

output = tk.Label(root, text="move mouse or press a key")
output.pack(pady=20)

def on_key(event):
    output.config(text=f"key pressed: {event.char}")

def on_click(event):
    output.config(text=f"Clicked at: {event.x}, {event.y}")

root.bind("<Key>", on_click)
root.bind("<Button>", on_click)


root.mainloop()



