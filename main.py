from tpblite import TPB
from urllib import parse
from SimpleTorrentStreaming import SimpleTorrentStreaming


def main():
    t = TPB()
    search = input('What do you want? ')
    torrents = t.search(search).getBestTorrent()
    torrent = torrents.magnetlink
    stream(torrents)


def stream(torrents):
    pass


    
if __name__ == "__main__":
    main()