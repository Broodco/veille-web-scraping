import requests
response = requests.get("https://fr.wikipedia.org/robots.txt")
robots = response.text
print (robots)
