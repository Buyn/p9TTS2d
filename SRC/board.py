"""
p2tts2d game.
"""

from gconstants import *
import arcade

class Board(arcade.Window):
    """ Window application class. """

    def __init__(self, _game):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.game = _game
        arcade.set_background_color(BOARD_BACKGROUND_COLOR)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()

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
