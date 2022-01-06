from bs4 import BeautifulSoup
import requests


url = 'https://1337x.to/'
response = requests.get(url)

if response.ok:
    print('Server is running')
else:
    print('Error with server')


