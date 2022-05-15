import subprocess
from tpblite import TPB
from tpblite import CATEGORIES
import random
from termcolor import colored
import os

start_again = True

def change_colors():
        colors = ['red', 'green', 'blue', 'yellow', 'grey', 'magenta', 'cyan']
        return random.choice(colors)


while start_again:
    torrent_dict = {}
    magnet_dict = {}

    accu = 0
    t = TPB('https://tpb.party')
    search = input(colored('What do you want to watch?: \n (M)ovie/(S)eries ', change_colors())).lower()


    if search == 'm':
        movie_name = input(colored('What Movie?: ', change_colors()))
        get_torrent = t.search(movie_name, category=CATEGORIES.VIDEO.MOVIES)

    elif search == 's':
        series_name = input('What series?: ')
        season = input('What Season?: ')
        episode = input('What Epsidode?: ')
        series = f'{series_name} s0{season} e0{episode}'
        
        print(f'Looking for {colored(series, change_colors())}')
        get_torrent = t.search(series, category=CATEGORIES.VIDEO.TV_SHOWS)

    if torrent_dict != True:
        print('Theres nothing to display. ')
        

    for title in get_torrent:
        torrent_dict[accu] = title.title
        magnet_dict[accu] = title.magnetlink
        accu += 1

    for item in torrent_dict:
        print(f'| {colored(item, change_colors())} | {colored(torrent_dict[item], change_colors())} |')


    select_dict = int(input(colored('Select a number: ', change_colors())))
    torrent_link = magnet_dict[select_dict]

    subprocess.call(['webtorrent', torrent_link, '--mpv'])

    re_start_again = input('Are you done?: Y/N: ').lower()
    if re_start_again == 'y':
        print('Bye-Bye')
        start_again = False
