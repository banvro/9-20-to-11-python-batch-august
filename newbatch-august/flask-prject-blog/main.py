from flask import Flask, render_template, request, flash, session
from flask import redirect
import mysql.connector
import os
from flask_mail import Mail, Message

conn = mysql.connector.connect(host="localhost", username = "root", password="1234", database = "amazon")
curser = conn.cursor()


web = Flask(__name__)
web.secret_key = "this isbdkjsdhvas "

web.config['MAIL_SERVER']='smtp.gmail.com'
web.config['MAIL_PORT'] = 465
web.config['MAIL_USERNAME'] = 'banvro07@gmail.com'
web.config['MAIL_PASSWORD'] = 'ubtl khhk pmjg nqze'
web.config['MAIL_USE_TLS'] = False
web.config['MAIL_USE_SSL'] = True
mail = Mail(web)



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
        session["username"] = fname
        if Image:
            Image.save(os.path.join("static/images", Image.filename))
            img = os.path.join("static/images/", Image.filename)

        curser.execute(f"insert into savemydataa values('{fname}', '{email}', '{p_number}', '{message}', '{img}')")
        conn.commit()

        msg = Message("This message send from Fask", sender = "banvro07@gmail.com", recipients = ["banvro07@gmail.com"])

        msg.body = f"""UserInfo:::
        Name = {fname}
        Email = {email}
        Phone NUmber = {p_number}
        Message = {message}"""
        mail.send(msg)

        flash("You data Saved sucessfulyy..!")

        return redirect("/showdata")
    

@web.route("/showdata")
def showdata():
    curser.execute("select * from savemydataa;")
    data = curser.fetchall()
    xyz = session.get("username")
    # print(data)
    return render_template("showdata.html", alldata = data, hey = xyz)


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

        flash("Your data updated sucessfully")

        return redirect("/showdata")



@web.route("/hlo/<name>")
def hlo(name):
    return f"hthis is helo ::::: {name}"

if __name__ == "__main__":
    web.run(debug = True)












