from flask import app
from flask import Flask
from flask import render_template    # Add this line
from .utils import get_latest_news 
app = Flask (__name__)

@app.route('/')
def say_hello():
    user = {"name": "Wangari"}
    return render_template("index.html", user=user)    # Modify this line
app.run(
    debug = True
)
@app.route('/news')
def news_headlines():
    news_articles = get_latest_news()
    return render_template("news.html", news_articles=news_articles)
