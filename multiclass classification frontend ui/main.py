# Tkinter
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import joblib
import numpy as np

model = joblib.load("fashion_images_predictor.joblib")

fasion_prodcuts = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

def upload_and_predict_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.thumbnail((400, 400))
    new_img = ImageTk.PhotoImage(img)
    image_show.config(image=new_img)
    image_show.image = new_img

    #to pass to model for prediction
    resize_img = img.convert("L").resize((28, 28))
    image_array = np.array(resize_img)
    convert_to_1d = image_array.flatten() #now data become 1d

    # chnage shape of data
    shaped_data = convert_to_1d.reshape(1, -1)
    
    pred = model.predict(shaped_data)[0]

    message.config(text = f"The Upload image is : {fasion_prodcuts[pred]}")

    

app = tk.Tk()
app.geometry("800x650")
app.config(background = "#44f238")
app.title("Fashion Image Predictor")

heading = tk.Label(app, text = "Fashion Image Predictor", font = ("robort", 30, "bold"), foreground = "white", background = "green")
heading.pack(fill = "x", ipady = 10)

image_show = tk.Label(app, background = "#44f238")
image_show.pack(pady = 13)

btn = tk.Button(app, text = "Upload to Predict", font = ("robort", 20, "bold"), foreground = "white", background = "green", command = upload_and_predict_image)
btn.pack()

message = tk.Label(app, background = "#44f238", font = ("robort", 17))
message.pack(pady = 13)


app.mainloop()


# 8219836118