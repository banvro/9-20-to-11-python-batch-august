import tkinter as tk
import mysql.connector
from tkinter import messagebox

myconn = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "afternoonbatch")

engine = myconn.cursor()


def savingdata():
    x = ent1.get()
    y = ent2.get()
    z = ent3.get()

    engine.execute(f"insert into newcontact values('{x}', '{y}', '{z}')")

    myconn.commit()

    messagebox.showinfo("Data Saved", "Your data saved sucessfully in database......!")

    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)



app = tk.Tk()
app.geometry("700x640")
app.title("Contact Us form")

frame1 = tk.Frame(app, relief = "groove", borderwidth = 20, bg = "green")
frame1.pack(fill = "x")

frame2 = tk.Frame(app, relief = "raised", borderwidth = 20, bg = "green")
frame2.pack(fill = "x")

lbl = tk.Label(frame1, text = "Contact Us", font = ("robort", 35, "bold"), fg = "white", bg = "green")
lbl.pack()

myimg = tk.PhotoImage(file = "contact us imagee.png")

showimg = tk.Label(frame2, image = myimg, height = 200)
showimg.pack()

frame3 = tk.Frame(app, relief = "sunken", borderwidth = 30, background = "green")
frame3.pack(fill = "x")


name = tk.Label(frame3, text = "Full Name", font = ("robort", 20, "bold"), background = "green", foreground = "white")
email = tk.Label(frame3, text = "Your email", font = ("robort", 20, "bold"), background = "green", foreground = "white")
message = tk.Label(frame3, text = "Message", font = ("robort", 20, "bold"), background = "green", foreground = "white")

blankk = tk.Label(frame3, text = "")

blankk.grid(row = 0, column = 0, padx = 20, pady = 5)
name.grid(row = 1, column = 1)
email.grid(row = 2, column = 1)
message.grid(row = 3, column = 1)



dotes1 = tk.Label(frame3, text = ":", background = "green", foreground = "white", font = ("robort", 20, "bold"))
dotes2 = tk.Label(frame3, text = ":", background = "green", foreground = "white", font = ("robort", 20, "bold"))
dotes3 = tk.Label(frame3, text = ":", background = "green", foreground = "white", font = ("robort", 20, "bold"))

dotes1.grid(row = 1, column = 2)
dotes2.grid(row = 2, column = 2)
dotes3.grid(row = 3, column = 2)


ent1 = tk.Entry(frame3, font = ("robort", 20, "bold"))
ent2 = tk.Entry(frame3, font = ("robort", 20, "bold"))
ent3 = tk.Entry(frame3, font = ("robort", 20, "bold"))

ent1.grid(row = 1, column = 3)
ent2.grid(row = 2, column = 3, pady = 10)
ent3.grid(row = 3, column = 3)

btn = tk.Button(frame3, text = "Submit", font = ("robort", 18, "bold"), background = "white", fg = "green", command = savingdata)
btn.grid(row = 4, column = 3, pady = 10, ipadx = 30)

app.mainloop()
