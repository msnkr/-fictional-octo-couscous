from tpblite import TPB
import os 


def main():
    t = TPB()
    search = input('What do you want? ')
    torrents = t.search(search).getBestTorrent()
    torrent = torrents.magnetlink
    run_webtorrent(torrent)

def run_webtorrent(torrent):
    cmd = f'webtorrent "{torrent}" --mpv --player-args="video-on-top"'
    os.system(cmd)


    
if __name__ == "__main__":
    main()