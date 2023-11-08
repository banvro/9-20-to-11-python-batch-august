from flask import Flask, render_template, request, redirect
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

# ORM : 

web=Flask(__name__)
web.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

db = SQLAlchemy(web)

class TodoSaveData(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String, nullable=False)
    descrption : Mapped[str] = mapped_column(String)

with web.app_context():
    db.create_all()

@web.route("/home")
def home():
    return render_template("basic_files/home2.html")

@web.route("/saveData", methods=["POST"])
def savedata():
    if request.method == "POST":
        Title = request.form.get("title")
        Description = request.form.get("description")

        save = TodoSaveData(title = Title, descrption = Description)
        db.session.add(save)
        db.session.commit()

        return redirect("/showdata")
    

@web.route("/showdata")
def showdata():
    data = TodoSaveData.query.all()
    print(data, "xxxxxxxxxxxxxx")
    return render_template("basic_files/showdata2.html",alldata=data)

@web.route("/deletedata/<x>", methods=["POST"])
def delete(x):
    return redirect("/showdata")

if __name__=="__main__":
    web.run(debug=True)