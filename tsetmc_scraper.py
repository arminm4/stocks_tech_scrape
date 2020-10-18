from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json


session = HTMLSession()
resp = session.get('http://tsetmc.com/Loader.aspx?ParTree=15131F')
print(resp)
resp.html.render(timeout = 120)
soup = BeautifulSoup(resp.html.html, 'html.parser')
result = soup.find('div', id = 'main')
children = result.children

i = 0
for child in children:
    i = 1
    print('child #', i, ' ', child) 

session.close()
