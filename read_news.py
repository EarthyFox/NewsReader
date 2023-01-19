import requests
import json
import time


url = 'https://newsapi.org/v2/everything?q=keyword&apiKey=e9a4f87a15ab4eb6bf6261f058bed9b9'
response = requests.get(url)
news = json.loads(response.text)

for new in news['articles']:
    print("##############################################################\n")
    print(str(new['title']))
    print('______________________________________________________\n')
    print(str(new['description']))
    print("..............................................................")
    time.sleep(2)