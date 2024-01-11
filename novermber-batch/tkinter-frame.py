import tkinter as tk

app = tk.Tk()
app.geometry("400x600")

frame1 = tk.Frame(app, relief = "groove", borderwidth = 20, background = "yellow")
frame1.pack(fill = "x")

frame2 = tk.Frame(app, relief = "ridge", borderwidth = 20, background = "green")
frame2.pack(fill = "x")

frame3 = tk.Frame(frame1, relief = "ridge", borderwidth = 20, background = "green")
frame3.pack(fill = "x")

lbl1 = tk.Label(frame1, text = "i am label 1", font = ("robort", 30, "bold"), bg = "yellow")
lbl1.pack(ipady = 20)

ent1 = tk.Entry(frame3)
ent1.pack(ipady = 20)

app.mainloop()