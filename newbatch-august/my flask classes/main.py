# pip install flask

from flask import Flask
from flask import render_template

myweb = Flask(__name__)


@myweb.route("/")
def home():
    return render_template("home.html", data = "this is dta")

@myweb.route("/contact")
def contactus():
    return render_template("contact.html")


@myweb.route("/about/<int:x>")
def aboutus(x):
    return render_template("about.html", data = x)




if __name__ == "__main__":
    myweb.run(port=1000, debug = True)






# jinja2 tamplate engain 