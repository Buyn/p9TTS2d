"""
p2tts2d game.
testing class 
2023-09-02
"""

import unittest
from unittest.mock import patch
from game import *

class Card():

    def __init__(self):
        self.mesage = []
        self.events = {"event_flip":self.flip_face,
                      }

    def flip_face(self, enput, args):
        self.mesage.append("event_flip")

class Test(unittest.TestCase):

    @classmethod 
    def setUpClass(self):
        self.test = Game()
        import board
        self.board = board.Board(self.test) 
        self.test_card = Card()

    def test_init(self):
        self.assertEqual( self.test.input.inputs["Left Click"], "event_flip")

    def test_left_click(self):
        self.test.mouse.on_click(0, 0, LEFT_CLICK, 0, self.test_card)
        self.assertEqual( self.test_card.mesage.pop(), "event_flip")

if __name__ == "__main__":
    unittest.main()
