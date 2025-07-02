from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/submit",methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username == "ritam008" and password == "pass":
    #     return render_template("welcome.html",name=username)
    valid_users = {
        'admin': '123',
        'ritam008': 'pass',
        'rajat': 'raj'
    }
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html",name=username)

    else:
        return "Invalid credentials"
