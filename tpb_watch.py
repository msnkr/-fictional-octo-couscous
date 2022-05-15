from tpblite import TPB
from tpblite import CATEGORIES
import random
from termcolor import colored
import os

start_again = True

while start_again:
    colors = ['red', 'green', 'blue', 'yellow', 'grey', 'magenta', 'cyan']
    random_color = random.choice(colors)

    torrent_dict = {}
    magnet_dict = {}

    accu = 0
    t = TPB('https://tpb.party')
    search = input(colored('What do you want to watch?: \n M/S ', random_color)).lower()


    if search == 'm':
        random_color = random.choice(colors)
        movie_name = input(colored('What Movie?: ', random_color))
        get_torrent = t.search(movie_name, category=CATEGORIES.VIDEO.MOVIES)

    elif search == 's':
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
        random_color = random.choice(colors)
        print(f'| {colored(item, random_color)} | {colored(torrent_dict[item], random_color)} |')

    random_color = random.choice(colors)
    select_dict = int(input(colored('Select a number: ', random_color)))
    torrent_link = magnet_dict[select_dict]

    play = os.system(f'webtorrent "{torrent_link}" --mpv')

    re_start_again = input('Are you done?: Y/N: ').lower()
    if re_start_again == 'y':
        print('Bye-Bye')
        start_again = False
