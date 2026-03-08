import requests
from config import api_key
from topics import topics

BASE_URL = "https://newsapi.org/v2/top-headlines"


def get_news(category):

    params = {
        "country": "in",
        "category": category,
        "apiKey": api_key
    }

    response = requests.get(BASE_URL, params=params)

    data = response.json()

    articles = data["articles"]

    for i, article in enumerate(articles[:5], start=1):
        print(f"\n{i}. {article['title']}")
        print(article["description"])
        print(article["url"])


print("\nChoose a news category:\n")

for key, value in topics.items():
    print(f"{key}. {value}")

choice = int(input("\nEnter choice: "))

if choice in topics:
    get_news(topics[choice])
else:
    print("Invalid choice")