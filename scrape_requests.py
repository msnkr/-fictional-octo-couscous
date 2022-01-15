from bs4 import BeautifulSoup
import requests
import pprint

html = 'https://1337x.to/torrent/5092042/Resident-Evil-Welcome-to-Raccoon-City-2021-1080p-AMZN-WEBRip-DDP5-1-x264-CM/'
response = requests.get(html)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.div['content-page'])
