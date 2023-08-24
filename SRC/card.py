"""
p2tts2d game.
Card sprite Game element class
2023-08-24
"""

from gconstants import *
import arcade
from gamelement import Gamelement

class Card(Gamelement):
    """ Card sprite game element """

    """ Card sprite game element """
    def __init__(self, keeper, suit, value, scale=1, x=START_X, y=BOTTOM_Y):
        """ Card constructor """
        # Attributes for suit and value
        self.suit = suit
        self.value = value
        # Image to use for the sprite when face up
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"
        # Call the parent
        super().__init__(keeper, self.image_file_name)
        self.position = x, y
