from tpblite import TPB
from tpblite import CATEGORIES

torrent_dict = {}
magnet_dict = {}

accu = 0
t = TPB('https://tpb.party')
search = input('What do you want to watch?: \n Movies or Series? ').lower()


if search == 'movies':
    movie_name = input('What Movie?: ')
    get_torrent = t.search(movie_name, category=CATEGORIES.VIDEO.MOVIES)
elif search == 'series':
    series_name = input('What series?: ')
    season = input('What Season?: ')
    episode = input('What Epsidode?: ')
    series = f'{series_name} s0{season} e0{episode}'
    print(series)
    get_torrent = t.search(series, category=CATEGORIES.VIDEO.TV_SHOWS)


for title in get_torrent:
    torrent_dict[accu] = title.title
    magnet_dict[accu] = title.magnetlink
    accu += 1

for item in torrent_dict:
    print(f'{item}: {torrent_dict[item]}')

select_dict = int(input('Select a number: '))
torrent_link = magnet_dict[select_dict]

