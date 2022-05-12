from tpb import TPB
from tpb import CATEGORIES


t = TPB('https://thepiratebay.org')
search = t.search('recipe book', category=CATEGORIES.VIDEO.MOVIES)

for torrent in t.search('resident evil'):
    print(torrent.info)
