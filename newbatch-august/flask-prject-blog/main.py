from flask import Flask, render_template, request
from flask import redirect
import mysql.connector

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
        curser.execute(f"insert into savemydata values('{fname}', '{email}', '{p_number}', '{message}')")
        conn.commit()

        return redirect("/showdata")
    

@web.route("/showdata")
def showdata():
    curser.execute("select * from savemydata;")
    data = curser.fetchall()
    # print(data)
    return render_template("showdata.html", alldata = data)


@web.route("/deletedata/<x>", methods = ["POST"])
def deletethis(x):
    curser.execute(f"delete from savemydata where Name = '{x}'")
    conn.commit()
    return redirect("/showdata")


@web.route("/showupdate/<x>", methods = ["POST"])
def updatedata(x):
    curser.execute(f"select * from savemydata where Name = '{x}'")
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
        curser.execute(f'update savemydata set Name = "{fname}", email = "{email}", Number = "{p_number}", message = "{message}" where Name = "{x}";')
        conn.commit()

        return redirect("/showdata")



@web.route("/hlo/<name>")
def hlo(name):
    return f"hthis is helo ::::: {name}"

if __name__ == "__main__":
    web.run(debug = True)












