import tkinter as tk

app = tk.Tk()

app.geometry("400x400")
# grid
labl = tk.Label(app, text = "this is my text")
labl.grid(row=0, column=0, padx=20)

btn = tk.Button(app, text = "subit")
btn.grid(row=1, column=0)




app.mainloop()