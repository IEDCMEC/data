import requests 
from bs4 import BeautifulSoup 
import os
import json
  
URL = "https://www.ecell.in/enspace/case.php"
r = requests.get(URL) 

names = []
links = []
pics = []

soup = BeautifulSoup(r.content, 'html5lib')
row = soup.find("div", attrs={'class': 'row', 'style': 'margin-top:10px'})
for p in soup.findAll('p'):
    names.append(p.text)

for a in soup.findAll('a'):
    links.append(a['href'])

for img in soup.findAll('img'):
    pics.append(img['src'])

names = names[:-4]
links = links[8:len(names) + 8]
pics = pics[:-1]

pics = ["images/" + os.path.basename(name) for name in pics]

data = []
for i in range(0, len(names)):
    data.append({"name": names[i], "link": links[i], "url": pics[i]})
print(json.dumps(data))