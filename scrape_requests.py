from tpblite import TPB
from tpblite import CATEGORIES

torrent_dict = {}
accu = 0
t = TPB('https://tpb.party')
search = input('What do you want to watch?: \n Movies or Series? ').lower()


if search == 'movies':
    movie_name = input('What Movie?: ')
    get_torrent = t.search(movie_name, category=CATEGORIES.VIDEO.MOVIES)
elif search == 'series':
    series_name = input('What series?: ')
    get_torrent = t.search(series_name, category=CATEGORIES.VIDEO.TV_SHOWS)


for title in get_torrent:
    torrent_dict[accu] = title.title
    accu += 1

for item in torrent_dict:
    print(f'{item}: {torrent_dict[item]}')

select_dict = int(input('Select a number: '))

