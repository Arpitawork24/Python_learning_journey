import requests
from config import api_key
from topics import topics

base_url = "https://newsapi.org/v2/top-headlines"

def get_news(category):
    params = {
    "country" : "in",
    "category" : category,
    "apiKey" = api_key
} 