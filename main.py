from tpblite import TPB
from simple_term_menu import TerminalMenu



def main():
    li = []
    t = TPB()
    search = input('What do you want? ')
    torrents = t.search(search)
    item = [str(torrents)]
    terminal_menu = TerminalMenu(item)
    menu_entry_index = terminal_menu.show()

if __name__ == "__main__":
    main()
main()