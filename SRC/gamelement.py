"""
p2tts2d game.
Game element class
2023-08-24
"""

from gconstants import *
import arcade

class Gamelement(arcade.Sprite):
    """ Game element sprite """

    def __init__(self, keeper, image_file_name, scale=1, hit_box_algorithm="None"):
        """ Game element constructor """
        # should be the default value for objects
        # image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"
        super().__init__(image_file_name, scale, hit_box_algorithm=hit_box_algorithm)
        self.keeper = keeper
        self.add_to_draw()
        # Call the parent

    def add_to_draw(self):
        self.keeper.add_to_draw(self)

    def remove_from_draw(self):
        self.keeper.remove_from_draw(self)
