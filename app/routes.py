from flask import render_template    
from .utils import get_latest_news 
from app import app

@app.route('/')
def say_hello():
    user = {"name": "Awesome Reader"}
    return render_template("index.html", user=user)    

@app.route('/news')
def news_headlines():
    '''
    Function that gets data from get_latest_news function
    '''
    news_articles = get_latest_news()
    return render_template("news.html", news_articles=news_articles)# render news.html file and passed the news_articles list.


