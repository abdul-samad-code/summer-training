# tkinter

import tkinter as tk
root = tk.Tk()       # Tk main /root window create karta hai
root.title("My Application")
width = 500
height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) //2
root.geometry(f"{width}x{height}+{x}+{y}")


root.configure(bg="lightblue")    # bg color 
root.resizable(True, False)

root.mainloop()      # it opens the window and wait for user action 


          