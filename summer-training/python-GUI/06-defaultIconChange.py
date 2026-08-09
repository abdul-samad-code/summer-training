import tkinter as tk
root = tk.Tk()
root.title('default icon change')
root.geometry("600x400+50+50")
root.resizable(False,False)
try:
    photo = tk.PhotoImage(file='/.assets/icon.png')
    root.iconphoto(False, photo)
except tk.TclError:
    print("icon file not dound.")
root.mainloop()