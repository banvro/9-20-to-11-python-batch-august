import tkinter as tk
import joblib

# y = mx + b 

def checkpkg():
    x = ent.get()
    model = joblib.load("myfirstplacmentmodel.joblib")
    m = model.coef_
    b = model.intercept_ 

    y = m * float(x) + b

    lblshow.config(text = f"Your Package is : {y[0]}")


app = tk.Tk()
app.title("Check Placemeent")
app.geometry("500x300")
app.config(background = "yellow")


lbl = tk.Label(app, text  = "Enter your CGPA", font = ("Arial", 20, "bold"), bg = "yellow")
lbl.pack(pady=20)

ent = tk.Entry(app, font = ("Arial", 20, ))
ent.pack()

btn = tk.Button(app, text = "Check PKG", font = ("Arial", 14, "bold"), command = checkpkg)
btn.pack(pady=20)

lblshow = tk.Label(app, text = "", font=("robort", 12),  fg = "blue", bg="yellow")
lblshow.pack()

app.mainloop()