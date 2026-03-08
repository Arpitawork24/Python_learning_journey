import requests
from config import api_key
from topics import topics

# Show available news categories to the user
for key, value in topics.items():
    print(f"{key}. {value}")

# Take user input for category selection
user_choice = int(input("Enter number: "))

# Validate user choice
if user_choice in topics:
    category = topics[user_choice]
else:
    print("Invalid choice")
    exit()

# Parameters sent to NewsAPI
params = {
    "apiKey": api_key,
    "country": "us",
    "category": category
}

# Send request to NewsAPI
response = requests.get("https://newsapi.org/v2/top-headlines", params=params)
print("Status Code:", response.status_code)

# Convert API response (JSON) into Python dictionary
data = response.json()

# Extract list of articles
articles = data["articles"]

# Display top 5 news articles
for article in articles[:5]:
    print("\nTitle:", article["title"])
    print("Description:", article.get("description"))
    print("URL:", article["url"])