from flask import Flask, request
app = Flask(__name__)

# spectfic webpage coonect specific connection
@app.route("/")
def home():
    return "Hello user! This is my first flask user"

@app.route("/about")
def about():
    return "This is about us page"

@app.route("/contact")

def contact():
    return "This is a contact page"


@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "You sent data"
    else:
        return "You are only viewing the form"



