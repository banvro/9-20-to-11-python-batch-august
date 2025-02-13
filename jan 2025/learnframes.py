import tkinter as tk
import mysql.connector
from tkinter import messagebox

mycon = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "morningbatch")

engine = mycon.cursor()


def savingdata():
    a = ent1.get()
    b = ent2.get()
    c = ent3.get("1.0", tk.END)

    engine.execute(f"insert into fortkinter values('{a}', '{b}', '{c}')")

    mycon.commit()

    messagebox.showinfo("Data Saved", "Your data saved successfully in database..!")

    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete("1.0", tk.END)


app = tk.Tk()
app.geometry("600x635")
app.title("Contact Us forms")

img = tk.PhotoImage(file = "contactt.png")


frame1 = tk.Frame(app, relief = "groove", borderwidth = 20, background = "darkgreen")
frame1.pack(fill = "x")

frame2 = tk.Frame(app, relief = "ridge", borderwidth = 20)
frame2.pack(fill = "x")

frame3 = tk.Frame(app, relief = "raised", borderwidth = 20, background = "green")
frame3.pack(fill = "x")



lbl = tk.Label(frame1, text = "Contact Us", font = ("robort", 34, "bold"), foreground = "white", bg = "darkgreen")
lbl.pack()

showimg = tk.Label(frame2, image = img, height = 200)
showimg.pack()


blank = tk.Label(frame3, text = "", background= "green")
blank.grid(row = 0, column = 0, padx = 30, pady = 5)

Name = tk.Label(frame3, text = "Full Name", font = ("robort", 16, "bold"), background = "green", foreground = "White")
Email = tk.Label(frame3, text = "Your Email", font = ("robort", 16, "bold"), background = "green", foreground = "White")
Message = tk.Label(frame3, text = "Message", font = ("robort", 16, "bold"), background = "green", foreground = "White")


Name.grid(row = 1, column = 1)
Email.grid(row = 2, column = 1)
Message.grid(row = 3, column = 1)

dotes1 = tk.Label(frame3, text = ":", font = ("robort", 16, "bold"), background = "green", foreground = "White")
dotes2 = tk.Label(frame3, text = ":", font = ("robort", 16, "bold"), background = "green", foreground = "White")
dotes3 = tk.Label(frame3, text = ":", font = ("robort", 16, "bold"), background = "green", foreground = "White")

dotes1.grid(row = 1, column = 2)
dotes2.grid(row = 2, column = 2)
dotes3.grid(row = 3, column = 2)

ent1 = tk.Entry(frame3, font = ("robort", 16, "bold"))
ent2 = tk.Entry(frame3, font = ("robort", 16, "bold"))
ent3 = tk.Text(frame3, font = ("robort", 16, "bold"), height=3, width = 20)

ent1.grid(row = 1, column = 3)
ent2.grid(row = 2, column = 3, pady = 13)
ent3.grid(row = 3, column = 3)

btn = tk.Button(frame3, text = "Submit", font = ("robort", 16, "bold"), background = "green", fg = "white", command = savingdata)
btn.grid(row = 4, column = 3, pady = 10)

app.mainloop()