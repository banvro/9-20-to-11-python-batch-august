import tkinter as tk
import joblib
import sklearn

modl = joblib.load("package-checker.joblib")

def checkpkg():
    cgpa = ent.get()

    # y = mx + b 

    m = modl.coef_
    b = modl.intercept_

    print(cgpa, "")
    print(type(cgpa), "")
    cgpa = float(cgpa)
    print(cgpa, type(cgpa))

    # y = m x + b 
    pkg = m[0] * cgpa + b
    pkg  =str(pkg)[0 : 4]
    lblshow.config(text=f"Your Package is : {pkg} Lakh.")

app = tk.Tk()
app.geometry("500x300")
app.title("Check your Package")


lbl = tk.Label(app, text = "Enter your CGPA", font = ("robort", 30, "bold"))
lbl.pack()

ent = tk.Entry(app, font = ("robort", 20, "italic"))
ent.pack(pady = 20)

btn = tk.Button(app, text = "Check CGPA", font = ("robort", 20, "bold"), command = checkpkg)
btn.pack()

lblshow = tk.Label(app, text = "", font = ("robort", 20, "italic"), fg = "green")
lblshow.pack(pady=20)


app.mainloop()