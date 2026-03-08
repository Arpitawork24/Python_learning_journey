import requests
from config import api_key
from topics import topics

for key, value in topics.items():
    print(f"{key}. {value}")

user_choice = int(input("enter no : "))

if user_choice in topics:
    category = topics[user_choice]
else:
    print("Invalid choice")
    exit()

params = {
    "apiKey" : api_key,
    "country" : "us",
    "category" : topics[user_choice]
}

response = requests.get("https://newsapi.org/v2/top-headlines", params=params)

print(response.status_code)

data = response.json()
# print(data["articles"]) # it will print all articles
articles = data["articles"] 
''' 
it will make articles look like these - 
[
 {article1},
 {article2},
 {article3}
]
'''

# print(articles[0])   it will print the full 1st article
# print(articles[0]["title"]) # it will print the title of 1st article


# Now it will print all news headlines.
# for article in articles:
    # print(article["title"])
    
# print("new")
for article in articles[:5]:
    print("title :", article["title"])
    print("description :", article.get("description"))
    print("url :", article["url"])