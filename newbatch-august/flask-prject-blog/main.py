from flask import Flask, render_template, request

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

    return f"nmae = {fname} , email = {email} phone number = {p_number} and message = {message}"

if __name__ == "__main__":
    web.run(debug = True)
