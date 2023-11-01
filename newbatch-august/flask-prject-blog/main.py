from flask import Flask, render_template, request
from flask import redirect
import mysql.connector
import os

conn = mysql.connector.connect(host="localhost", username = "root", password="1234", database = "amazon")
curser = conn.cursor()


web = Flask(__name__)

@web.route("/")
def home():
    return render_template("home.html")

@web.route("/about")
def about():
    return render_template("about.html")

@web.route("/contact")
def contact():
    return render_template("contact.html")

@web.route("/services")
def services():
    return render_template("services.html")

@web.route("/savedata", methods = ["POST"])
def savedata():
    if request.method == "POST":
        fname = request.form.get("fullname")
        # x = request.form["fullname"]
        email = request.form.get("email")
        p_number = request.form.get("number")
        message = request.form.get("msg")
        Image = request.files.get("img")

        if Image:
            Image.save(os.path.join("static/images", Image.filename))
            img = os.path.join("static/images/", Image.filename)

        curser.execute(f"insert into savemydataa values('{fname}', '{email}', '{p_number}', '{message}', '{img}')")
        conn.commit()

        return redirect("/showdata")
    

@web.route("/showdata")
def showdata():
    curser.execute("select * from savemydataa;")
    data = curser.fetchall()
    # print(data)
    return render_template("showdata.html", alldata = data)


@web.route("/deletedata/<x>", methods = ["POST"])
def deletethis(x):
    curser.execute(f"delete from savemydataa where Name = '{x}'")
    conn.commit()
    return redirect("/showdata")


@web.route("/showupdate/<x>", methods = ["POST"])
def updatedata(x):
    curser.execute(f"select * from savemydataa where Name = '{x}'")
    record = curser.fetchone()
    return render_template("updatedata.html", data = record)

@web.route("/updatenow/<x>", methods = ["POST"])
def updatenow(x):
    if request.method == "POST":
        fname = request.form.get("fullname")
        # x = request.form["fullname"]
        email = request.form.get("email")
        p_number = request.form.get("number")
        message = request.form.get("msg")
        curser.execute(f'update savemydataa set Name = "{fname}", email = "{email}", Number = "{p_number}", message = "{message}" where Name = "{x}";')
        conn.commit()

        return redirect("/showdata")



@web.route("/hlo/<name>")
def hlo(name):
    return f"hthis is helo ::::: {name}"

if __name__ == "__main__":
    web.run(debug = True)












