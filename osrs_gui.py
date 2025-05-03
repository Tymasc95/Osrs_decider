import os
from tkinter import *

script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct absolute path to the image
icon_path = os.path.join(script_dir, "OSRS_logo.png")

window = Tk()
window.geometry("400x400")
window.title("OSRS Task Generator")

icon = PhotoImage(file=icon_path)
window.iconphoto(True, icon)

window.mainloop()