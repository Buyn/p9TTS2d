"""
p2tts2d game.
"""

from gconstants import *
from card import Card
import arcade

class Board(arcade.Window):
    """ Window application class. """

    def __init__(self, _game):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.game = _game
        arcade.set_background_color(BOARD_BACKGROUND_COLOR)
        # Game elements list with all the elements, no matter what pile they are in.
        self.elements_list = arcade.SpriteList()

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Sprite list with all the cards, no matter what pile they are in.
        self.elements_list = None
        self.elements_list = arcade.SpriteList()
        # Create every card
        count=0
        for card_suit in CARD_SUITS:
            for card_value in CARD_VALUES:
                count +=1
                card = Card(self,
                            card_suit,
                            card_value,
                            x=START_X+count,
                            y=BOTTOM_Y+count)
                # добаить смешение на пиксель

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()
        # Draw the elements
        self.elements_list.draw()

    def add_to_draw(self, sprite):
        """ add to list of sprits to draw on screen """
        self.elements_list.append(sprite)

    def remove_from_draw(self, sprite):
        """ remove from list sprits to draw on screen """
        self.elements_list.remove(sprite)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        pass
