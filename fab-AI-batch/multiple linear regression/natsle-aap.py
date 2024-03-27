import tkinter as tk
import joblib

mymodel = joblib.load("nestle-model.joblib")

m = mymodel.coef_
b = mymodel.intercept_

def chekcthis():
    x = ent1.get()
    y = ent2.get()

    z = b + int(x) * m[0] + int(y) * m[1]
    
    lblshow.config(text = f"Total Turnover (Rs.) Deliverable : {z}")


app = tk.Tk()

app.geometry("500x600")
app.title("Nestle Price Pridction")


lbl1 = tk.Label(app, text =  "Enter No.of Shares", font=('Helvetica', 17, "bold"))
ent1 = tk.Entry(app, font=('Helvetica', 24, "italic"))

lbl2 = tk.Label(app, text =  "Enter No. of Trades", font=('Helvetica', 17, "bold"))
ent2 = tk.Entry(app, font=('Helvetica', 24, "italic"))

btn = tk.Button(app, text = "check", font=('Helvetica', 16, "bold"), command = chekcthis)

lblshow = tk.Label(app, text =  "", font=('Helvetica', 15, "italic"), fg = "green")

lbl1.pack(pady=15)
ent1.pack(pady=15)
lbl2.pack(pady=15)
ent2.pack(pady=15)

btn.pack()

lblshow.pack()



app.mainloop()