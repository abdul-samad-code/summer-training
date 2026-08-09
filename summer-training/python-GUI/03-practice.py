
#   Remove blury UI

import tkinter as tk
root = tk.Tk()
message = tk.Label(root, text="hello, world",)
message.pack()

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()