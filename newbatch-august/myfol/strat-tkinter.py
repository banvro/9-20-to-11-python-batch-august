# Tkinter 

import tkinter as tk
app = tk.Tk()


app.geometry("500x400")
app.title("My FIrst Tkinter App")
app.configure(background="red")

lbl = tk.Label(app, text = "Hwllo World !", font=("cursive", 20, "bold"), fg="white", bg="black")
lbl.pack(fill="x", padx = 30, pady = 20, ipady=10)

entr = tk.Entry(app, font=("Gill Sans", 20))
entr.pack(ipadx=20, ipady=10)

btn = tk.Button(app, text = "Submit", font=("cursive", 10, "bold"))
btn.pack(pady=20)

app.mainloop()


# 1) pack()
# 2) grid()
# 3) place()



