import sys
import random
from forbiddenfruit import curse
from . import screen

QUOTES = [
    "Scranton, the electric city.",
    "Oh God, my mind is going a mile an hour.",
    "Sometimes I'll start a sentence and I don't even know where it's going."
    " I just hope I find it along the way.",
    "I am running away from my responsibilties. And it feels good.",
    "Should have burned this place down when I had the chance.",
    "I'm not superstitious, but I am a little stitious.",
    "Bears. Beets. Battlestar Gallactica.",
    "Why waste time say lot word when few word do trick?",
]


def __mifflin__(self):
    if sys.stdout.isatty():
        # if in the terminal display ascii art, otherwise just return
        screen.play_screen()
    return random.choice(QUOTES)


curse(object, "__mifflin__", __mifflin__)
