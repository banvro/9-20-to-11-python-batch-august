# Tkinter : 
# pygame 
# pyqt5

import tkinter as tk
from tkinter import messagebox

def showmsgbox():
    print("helooooooo")
    messagebox.showwarning("Data Saved", "Your Data Saved Sucessfully in Database..!")
    # messagebox.showinfo("Data Saved", "Your Data Saved Sucessfully in Database..!")

window = tk.Tk()
window.geometry("500x300")
window.title("This is my Title")
window.config(background = "green")

lbl = tk.Label(window, text = "Hellow wolrd", font = ("robort", 30, "bold"), fg = "red", bg = "yellow")
lbl.pack(fill = "x", padx = 30, pady = 30, ipady = 10, side = "top")

en = tk.Entry(window, font = ("robort", 20, "italic"))
en.pack()

btn = tk.Button(window, text = "Submit", font = ("robort", 20, "bold"), command = showmsgbox)
btn.pack(pady = 20)

window.mainloop()


# 1) pack()
# 2) grid()
# 3) place()















