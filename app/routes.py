from app import app

from flask import render_template    # Add this line


@app.route('/')
def say_hello():
    user = {"name": "Wangari"}
    return render_template("index.html", user=user)    # Modify this line
