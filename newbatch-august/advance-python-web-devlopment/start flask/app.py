from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about/<x>")
def about(x):
    return f"the id is : {x}"

@app.route("/contact")
def y():
    return render_template("contact.html")
    # return "this is my concat  page"

if __name__ == "__main__":
    app.run(debug = True)