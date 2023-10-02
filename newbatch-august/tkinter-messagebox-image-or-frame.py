# # 1) message box 
# # 2) show image 

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("400x300")


frma1 = tk.Frame(window, bg="red", height=200, width=100, relief = "solid", borderwidth=12)
frma1.pack(side="left", fill="y")


# lbl = tk.Label(frma1, text="helloooo")
# lbl.pack()




img = Image.open("car.jpg")

imgx = ImageTk.PhotoImage(img)


lbl = tk.Label(frma1, text="hellow word", image=imgx)
lbl.pack()


window.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk

# def chnagecurency():
#     qw = ent.get()
#     zx = int(qw) * 80
#     messagebox.showerror("chnage", f"the total inr : {zx}")

# img = Image.open("car.jpg")
# imgx = ImageTk.PhotoImage(img)

# app = tk.Tk()
# app.geometry("600x400")

# f1 = tk.Frame(app, relief="groove", bg="yellow", height=100, width=100)
# f1.grid(row=0, column=0)

# f2 = tk.Frame(app, relief="groove", bg="black")
# f2.grid(row=1, column=0)


# lbl = tk.Label(f1, text = "Enter your USD : ", bg = "yellow", font=("Robort", 20, "bold"))
# lbl.grid(row=0, column=0, padx=30, pady=30, ipadx=10, ipady=10)

# ent = tk.Entry(f1, font=("Robort", 20, "italic"))
# ent.grid(row=0, column=1)

# btn = tk.Button(f1, text = "Change Currency", font=("Robort", 13, "bold"), command=chnagecurency)
# btn.grid(row=1, column=1)




# blx = tk.Label(f2, text="ajhds", image=imgx)
# blx.pack()

# app.mainloop()






# messagebox
# frames
# image



