# Tkinter : 
# pygame 
# pyqt5

import tkinter as tk

def calculateage():
    zx = en.get()

    age = 2024 - int(zx)
    en.delete(0, tk.END)

    lblsh.config(text = f"Your Age is : {age}")

window = tk.Tk()
window.geometry("500x350")
window.title("This is my Title")
window.config(background = "green")

lbl = tk.Label(window, text = "Hellow wolrd", font = ("robort", 30, "bold"), fg = "red", bg = "yellow")
lbl.pack(fill = "x", padx = 30, pady = 30, ipady = 10, side = "top")

en = tk.Entry(window, font = ("robort", 20, "italic"))
en.pack()

btn = tk.Button(window, text = "Submit", font = ("robort", 20, "bold"), command = calculateage)
btn.pack(pady = 20)

lblsh = tk.Label(window, text = "", font = ("robort", 20, "italic"), background = "green", fg = "red")
lblsh.pack()

window.mainloop()


# 1) pack()
# 2) grid()
# 3) place()















