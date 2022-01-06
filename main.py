from tpblite import TPB
import os 


def main():
    i = 0
    t = TPB()
    search = input('What do you want? ')
    torrents = t.search(search)
    for torrent in torrents:
        i += 1
        print(i, torrent)

    

    
# def run_webtorrent(torrent):
#     cmd = f'webtorrent "{torrent}" --mpv --player-args="video-on-top"'
#     os.system(cmd)


if __name__ == "__main__":
    main()