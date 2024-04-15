import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import joblib
import numpy as np

app = tk.Tk()
app.geometry("500x400")
app.title("image classification")

mymodel = joblib.load("image-classification.joblib")

def classifyimage(imgpath):
    img = Image.open(imgpath)
    imgresize = img.resize((28, 28))
    img_array = np.array(imgresize)
    img_flatten = img_array.flatten()
    img_final = img_flatten.reshape(1, -1)
    xyz = mymodel.predict(img_final)

    return xyz[0]

def uploadimgxyz():
    filepath = filedialog.askopenfilename()
    img = Image.open(filepath)
    imgn = ImageTk.PhotoImage(img)
    lblimg.config(image=imgn)

    lblimg.image = imgn

    predict = classifyimage(filepath)
    lblrecit.config(text = f"The image class is : {predict}")



lbl = tk.Label(app, text="Image Classification", font=("Arial Bold", 20))
lbl.pack()

lblimg = tk.Label(app)
lblimg.pack()

uploadimg = tk.Button(app, text = "Upload Image", font=("Arial Bold", 15), command = uploadimgxyz)
uploadimg.pack()

lblrecit = tk.Label(app, text = "", font=("arial", 16))
lblrecit.pack()


app.mainloop()