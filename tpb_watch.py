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


def play_torrent(torrent_dict, magnet_dict):
    if torrent_dict != True:
        print(colored('Theres nothing to show...', change_colors()))
        search_torrent()
    else:
        for item in torrent_dict:
            print(f"| {colored(item, change_colors())} | {colored(torrent_dict[item], change_colors())} |")

    select_dict = int(input(colored('Select a number: ', change_colors())))
    torrent_itself = magnet_dict[select_dict]

    subprocess.call(['webtorrent', torrent_itself, '--mpv'])


def search_torrent():
    torrent_dict = {}
    magnet_dict = {}
    accu = 1

    t = TPB('https://tpb.party')
    search = input(colored('What do you want to watch? A (M)ovie or (S)eries?: ', change_colors())).lower()

    if search == 'm':
        movie_name = input(colored('Whats the movie name?: ', change_colors())).lower()
        get_torrent = t.search(movie_name, category=CATEGORIES.VIDEO.MOVIES)

    elif search == 's':
        series_name = input(colored('Whats the series name?: ', change_colors())).lower()
        series_season = int(input(colored('What Season?: ', change_colors())))
        series_episode = int(input(colored('What Episode?: ', change_colors())))
        full_series = f'{series_name} s0{series_season} e0{series_episode}'

        get_torrent = t.search(full_series, category=CATEGORIES.VIDEO.TV_SHOWS)


    for title in get_torrent:
        torrent_dict[accu] = title.title
        magnet_dict[accu] = title.magnetlink
        accu += 1 

    play_torrent(torrent_dict, magnet_dict)


search_torrent()
