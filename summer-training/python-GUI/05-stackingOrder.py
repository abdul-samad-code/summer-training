import tkinter as tk
root = tk.Tk()
root.title('stacking order')
root.geometry("600x400+50+50")
root.resizable(False, False)
root.attributes('-topmost')
root.mainloop()