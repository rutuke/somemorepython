import os
from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World, This is Ruta"

@app.route("/colors")
def render_colors():
    return render_template("colors.html")

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    user_email = form_data["email"]
    text_email =form_data["text"]
    
    response = requests.post(
        "https://api.mailgun.net/v3/sandbox8532e1b21f364fc98df62c333450a10b.mailgun.org/messages",
        auth=("api", "key-36937666dd1e5f53438a11d957ec83a9"),
        data={"from": "Excited User <mailgun@sandbox8532e1b21f364fc98df62c333450a10b.mailgun.org>",
              "to": user_email,
              "subject": "Hello",
              "text": text_email})
    return response.text


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))