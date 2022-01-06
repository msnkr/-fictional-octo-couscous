from tpblite import TPB
import os 


def main():
    t = TPB()
    search = input('What do you want? ')
    torrents = t.search(search)
    for num, torrent in enumerate(torrents, start=1):
        print(num, torrent)

    answer = int(input('Select which one you want to watch: '))

    
# def run_webtorrent(torrent):
#     cmd = f'webtorrent "{torrent}" --mpv --player-args="video-on-top"'
#     os.system(cmd)


if __name__ == "__main__":
    main()