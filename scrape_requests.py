from bs4 import BeautifulSoup
import requests


url = 'https://1337x.to/'
response = requests.get(site)
if response.ok:
    print('All Good')
else:
    print('Something is wrong!')