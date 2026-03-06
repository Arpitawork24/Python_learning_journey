# The requests module is used to send HTTP requests to websites.
# In simple words, it lets your Python program ask data from the internet

import requests

response = requests.get("https://api.github.com")

print(response)

# When you request data from many APIs, the server sends data in JSON format.
# Python converts the JSON data from the website into a Python dictionary.
print(response.json)
# Now data becomes a dictionary containing information from GitHub's API.

response2 = requests.get("https://api.github.com/users/CodeWithHarry")

data = response2.json()

print(data["login"])
print(data["id"])
print(data["followers"])