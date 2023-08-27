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
        self.mouse = _game.mouse
        arcade.set_background_color(BOARD_BACKGROUND_COLOR)
        # Game elements list with all the elements, no matter what pile they are in.
        self.elements_list = arcade.SpriteList()

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Sprite list with all the elements, no matter what pile they are in.
        self.elements_list = None
        self.elements_list = arcade.SpriteList()
        # reset heldet elements
        self.mouse.setup()
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

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()
        # Draw the elements
        self.elements_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        if self.mouse.set_on_mouse_press(x, y, button, key_modifiers, self):
            return

    def on_mouse_release(self, x: float, y: float, button: int,
                         key_modifiers: int):
        """ Called when the user presses a mouse button. """
        if self.mouse.set_on_mouse_release(x, y, button, key_modifiers, self):
            return

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        if self.mouse.set_on_mouse_motion(x, y, dx, dy, self):
            return

    def add_element(self, element):
        self.elements_list.append(element)

    def remove_element(self, element):
        self.elements_list.remove(element)

    def pull_to_top(self, element: arcade.Sprite):
        """ Pull element sprite to top of rendering order (last to render, looks on-top) """
        # Remove, and append to the end
        self.elements_list.remove(element)
        self.elements_list.append(element)

if __name__ == "__main__":
    print("testin Board")
    from game import Game
    game = Game()
    board = Board(game)
    assert(board != None)
    # board.on_mouse_motion(1,2,3,4,6,board)
    board.on_mouse_press(1,2,3,4)
    board.on_mouse_motion(1,2,3,4)
    board.on_mouse_release(1,2,3,4)
