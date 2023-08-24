"""
p2tts2d game.
"""

import arcade
import gconstants
from game import Game
from board import Board

game = Game()
boards = [Board(game)]

def main():
    """ Main function """
    boards[0].setup()
    game.run()

if __name__ == "__main__":
    main()
