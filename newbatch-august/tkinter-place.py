import tkinter as tk
app = tk.Tk()

app.geometry("400x400")


lbl = tk.Label(app, text="this is pace1", font=("robort", 18, "bold"))
lbl.place(x = 100, y = 100)

lbl1 = tk.Label(app, text="this is pace2", font=("robort", 18, "bold"))
lbl1.place(x = 200, y = 200)

lbl2 = tk.Label(app, text="this is pace3", font=("robort", 18, "bold"))
lbl2.place(x = 100, y = 300)

lbl3 = tk.Label(app, text="this is pace4", font=("robort", 18, "bold"))
lbl3.place(x = 400, y = 400)

app.mainloop()