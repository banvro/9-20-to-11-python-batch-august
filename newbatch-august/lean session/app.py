from flask import Flask, session, make_response, request

app = Flask(__name__)
app.secret_key = "ksjdbfskjxkasdadasdsadsadsa"

@app.route("/")
def home():
    # session["token"] = "akjdbkasbdjkasbkdbksabdaksabdsakjdsbakd"
    # return "Session set sucessfyly"
    abc = make_response("cookies set")
    abc.set_cookie("userid", "123176313")
    return abc

@app.route("/get")
def getdata():
    x = request.cookies.get("userid")
    return f"the userid is : {x}"
    # if "token" in session:
    #     x = session.get("token")
    #     return f"User login as : {x}"
    # else:
    #     return "please lgin first"


@app.route("/dlt")
def dltsesion():
    zx = make_response("coolkie clear")
    zx.set_cookie("userid", " ", expires=0)
    # session.pop("token")
    return zx


if __name__=="__main__":
    app.run(debug=True, port = 1000)



# set session :  session["key"] = "value"
# get session :  session.get("key")
# delete session : session.pop("key")
# clear session  : session.clear()


# set cookes = x.set_cookies("key", "value")
# get cookies : request.cookies.get("key")
# delete cookies : zx.set_cookie("userid", " ", expires=0)