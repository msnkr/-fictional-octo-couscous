from tpblite import TPB
from simple_term_menu import TerminalMenu


def main():
    t = TPB()
    search = input('What do you want? ')
    torrents = t.search(search).getBestTorrent()
    return stream(torrents)

def stream(torrents):
    pass


    
if __name__ == "__main__":
    main()