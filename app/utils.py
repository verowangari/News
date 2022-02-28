import requests
from decouple import config

# from app.routes import sources

NEWS_API_KEY = config('NEWS_API_KEY')
COUNTRY = 'us'



def get_latest_news():
    '''
    Function that gets the json response to our url request
    '''
    news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country={COUNTRY}&apiKey={NEWS_API_KEY}').json()
    return news_data['articles']
def get_sources():
    '''
    Function that gets response for sources
    '''
    sources_data=requests.get(f"https://newsapi.org/v2/top-headlines/sources?apiKey=26e92efd5ae74abf9827342828a892d9")
    return sources_data['sources']