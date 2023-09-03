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
    def __init__(self, keeper, suit=None, value=None, resources_name=None, scale=1, x=START_X, y=BOTTOM_Y):
        """ Card constructor """
        # Attributes for suit and value
        self.suit = suit
        self.value = value
        # Image to use for the sprite when face up
        if resources_name:
            image_file_name = resources_name
        elif suit and value:
            image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"
        else:
            image_file_name = None
        # Call the parent
        super().__init__(keeper,
                         image_file_name_face_up = image_file_name,
                         image_file_name_face_down = CARD_FACE_DOWN_IMAGE,
                         scale=scale, hit_box_algorithm="None")
        self.face_down()
        self.position = x, y
        self.add_event("event_flip", self.face_flip)

if __name__ == "__main__":
    print("testin MouseHandler")
    test = MouseHandler("input")
    assert(test.set_on_mouse_release(1,2,3,4))
    test.on_left_double_clik(1,2,3,4)
