from time import sleep
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from . import office_opening


def office_screen_ascii(screen):
    for frame in office_opening.FRAMES:
        # split frame to lines and print line by line
        lines = frame.split()
        for i in range(len(lines)):
            screen.print_at(lines[i], 0, i)
        screen.refresh()
        sleep(0.2)
    sleep(1)


def play_screen():
    try:
        Screen.wrapper(office_screen_ascii)
    except ResizeScreenError:
        pass
