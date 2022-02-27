from flask import app
from flask import Flask
from flask import render_template    # Add this line

app = Flask (__name__)

@app.route('/')
def say_hello():
    user = {"name": "Wangari"}
    return render_template("index.html", user=user)    # Modify this line
app.run(
    debug = True
)
