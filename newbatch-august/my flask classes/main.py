# pip install flask

from flask import Flask
from flask import render_template

myweb = Flask(__name__)


@myweb.route("/")
def home():
    return render_template("basicfiles/home.html")

@myweb.route("/contact")
def contactus():
    return render_template("basicfiles/contact.html")


if __name__ == "__main__":
    myweb.run(port=1000, debug = True)