import os
from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

# @app.route("/")
# def hello():
#     return "Hello World, This is Ruta"

# @app.route("/colors")
# def render_colors():
#     return render_template("colors.html")

# @app.route("/<name>")
# def hello_someone(name):
#     return render_template("hello.html", name=name.title())

# @app.route("/signup", methods=["POST"])
# def sign_up():
#     form_data = request.form
#     print form_data["email"]
#     user_email = form_data["email"]
#     text_email =form_data["text"]
    
#     response = requests.post(
#         "https://api.mailgun.net/v3/sandbox8532e1b21f364fc98df62c333450a10b.mailgun.org/messages",
#         auth=("api", "key-#######"),
#         data={"from": "Excited User <mailgun@sandbox8532e1b21f364fc98df62c333450a10b.mailgun.org>",
#               "to": user_email,
#               "subject": "Hello",
#               "text": text_email})
#     return response.text

@app.route("/weather")
def get_weather():
    
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    payload = {"q": "London,UK", "units":"metric", "appid":"2caad4ac2e664ae96dd2e6b2327298fd"}
    response = requests.get(endpoint, params=payload)
    data = response.json()
    
    print(data["main"])
    print(response.url)
    print(response.status_code)
    print(response.headers["content-type"])
    print(response.text)
    
    temperature = data["main"]["temp"]
    name = data["name"]
    weather = data["weather"][0]["main"]
    print (u"It's {}C in {}, and the sky is {}".format(temperature, name, weather))
    
    return str(temperature)
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

