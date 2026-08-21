import tkinter as tk

root = tk.Tk()
root.title("Canvas Widget")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

canvas.create_rectangle(20, 20, 120, 100, fill="lightblue", outline="navy")
canvas.create_oval(140, 20, 240, 100, fill="orange", outline="black")
canvas.create_line(20, 120, 240, 120, fill="green", width=3)
canvas.create_text(130, 160, text="GIHSM", font=("Arial", 12, "bold"))


root.mainloop()
