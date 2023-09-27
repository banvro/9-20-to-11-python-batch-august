import tkinter as tk
import mysql.connector


conn = mysql.connector.connect(host = "localhost", username = "root", password="1234", database = "morning")

couser = conn.cursor()

# couser.execute("ajsdashdvk"

def savedata():
    en1 = entr1.get()
    en2 = entr2.get()
    en3 = entr3.get()
    
    couser.execute(f"insert into savedata values('{en1}', '{en2}', '{en3}')")
    conn.commit()

    entr1.delete(3, tk.END)
    entr2.delete(0, tk.END)
    entr3.delete(0, tk.END)

    labl7.config(text="Data save sucessfully...!")
    # cusers.excute(f"inser into tablename values('{en1}', {en2}, 'xyz@gmail.com')")

app = tk.Tk()

app.geometry("900x400")
app.title("My Form")
# grid
labl1 = tk.Label(app, text = "Name ", font=("robort", 20, "bold"))
labl2 = tk.Label(app, text = "Phone Number", font=("robort", 20, "bold"))
labl3 = tk.Label(app, text = "Email", font=("robort", 20, "bold"))
labl4 = tk.Label(app, text = ":", font=("robort", 20, "bold"))
labl5 = tk.Label(app, text = ":", font=("robort", 20, "bold"))
labl6 = tk.Label(app, text = ":", font=("robort", 20, "bold"))
labl7 = tk.Label(app, text="", font=("robort", 15, "bold"))

entr1 = tk.Entry(app, font=("robort", 20, "italic"))
entr2 = tk.Entry(app, font=("robort", 20, "italic"))
entr3 = tk.Entry(app, font=("robort", 20, "italic"))

btn = tk.Button(app, text="Submit", font=("robort", 20, "bold"), command=savedata)


labl1.grid(row=0, column=0, pady=10)
labl2.grid(row=1, column=0, pady=10, padx=50)
labl3.grid(row=2, column=0, pady=10)
entr1.grid(row=0, column=2, pady=10)
entr2.grid(row=1, column=2, pady=10)
entr3.grid(row=2, column=2, pady=10)
btn.grid(row=3, column=1, pady=10)

labl7.grid(row=4, column=1)


labl4.grid(row=0, column=1)
labl5.grid(row=1, column=1)
labl6.grid(row=2, column=1)






app.mainloop()