import tkinter as tk
from PIL import Image, ImageTk

# PIL
# pip install pillow

app = tk.Tk()
app.geometry("600x500")
app.title("show image")

x = Image.open("naturee.jpg")
img = ImageTk.PhotoImage(x)

lbl = tk.Label(app, text = "this is car", height = 100, width=300, image = img)
lbl.pack()


app.mainloop()