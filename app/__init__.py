from flask import Flask
from config import DevelopmentConfig

app = Flask(__name__)#create a relative path
app.config.from_object(DevelopmentConfig)

from app import routes
