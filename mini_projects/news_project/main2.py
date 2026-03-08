import requests
from config import api_key

params = {
    "apiKey" : api_key,
    "country" : "us",
    "category" : "technology"
}

response = requests.get("https://newsapi.org/v2/top-headlines", params=params)

print(response)

data = response.json()
print(data["articles"])