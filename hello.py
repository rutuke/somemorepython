import os
from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World, This is Ruta"

@app.route("/colors")
def render_colors():
    return render_template("colors.html")

@app.route("/signup")
def render_signup():
    return render_template("signup.html")

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))