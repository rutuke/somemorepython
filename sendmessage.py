import os
from flask import Flask, render_template, request, requests

app = Flask("MyApp")

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox8532e1b21f364fc98df62c333450a10b.mailgun.org/messages",
        auth=("api", "key-36937666dd1e5f53438a11d957ec83a9"),
        data={"from": "Excited User <mailgun@sandbox8532e1b21f364fc98df62c333450a10b.mailgun.org>",
              "to": ["c14314736@mydit.ie"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
              
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))