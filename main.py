import curses
from curses import wrapper
import os

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 20, "Hello World!") 
    stdscr.refresh()
    stdscr.getch()

    name = os.getenv("DB_NAME")
    print(name)

wrapper(main)
