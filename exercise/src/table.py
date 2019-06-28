import requests
from bs4 import BeautifulSoup
import json

website_url = requests.get('https://github.com/BertrandMarlair?tab=repositories').text

soup = BeautifulSoup(website_url,'html.parser')

repos = soup.find('div',{'id':'user-repositories-list'})

reposList = repos.findAll('li',{'itemprop':'owns'})

table = []

for repo in reposList:
    name = repo.find('h3').get_text(strip=True)
    try:
        desc = repo.find('p',{'itemprop':'description'}).get_text(strip=True)
    except:
        desc = 'Pas de description'
    repository = {
        'name' : name,
        'description' : desc
    }
    table.append(repository)

JSON_table = json.dumps(table, indent=4)

print(JSON_table)
