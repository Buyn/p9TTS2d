"""
p2tts2d game.
"""

import arcade
from gconstants import *
from InputHandler import InputHandler
from MouseHandler import MouseHandler

class Game():
    """ Start application class. """

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.input = InputHandler()
        self.mouse = MouseHandler(self.input)
        self.set_input()

    def set_input(self):
        self.input.set_input("Left Click", "left_click")
        self.input.set_input("Left Realise", "left_realise")
        self.input.set_input("On Pull", "on_pull")
        self.input.set_input("On Drop", "on_drop")
        self.input.set_input("On Move", "on_move")

    def run(self):
        """ Start game loop function """
        arcade.run()
if __name__ == "__main__" :
    print("testin Gamelement")
    # import game
    game = Game()
    import board
    board = board.Board(game)
    image_file_name = f":resources:images/cards/cardHeartsA.png"
    # CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]
    test = Gamelement(board, image_file_name)
    assert(test != None)
    # test.on_left_double_clik(1,2,3,4)
