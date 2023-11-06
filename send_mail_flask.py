from flask import Flask, session, make_response, request
from flask_mail import Mail, Message
app = Flask(__name__)
app.secret_key = "kasbjdk"

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'banvro07@gmail.com'
app.config['MAIL_PASSWORD'] = 'kqor ndvk cczf xeky'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/send_email')
def index():
   msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['programography@gmail.com'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"

@app.route("/")
def home():
   res = make_response("cookies set")
   res.set_cookie("xyz", "1234121212")
   return res

@app.route("/get")
def get():
    ab = request.cookies.get("xyz")
    return "s"

@app.route("/dlt")
def rem():
    resp = make_response("cocoke dlt")
    resp.set_cookie("xyz", "", expires=0)
    return resp

if __name__ == "__main__":
    app.run(debug=True)


# session["key"] = value
# z = session.get("key")
# session.pop("key")
# to clear all sessions : ::: session.clear()
