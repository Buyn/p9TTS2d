"""
p2tts2d game.
Mouse Handler Game class
2023-08-26
"""

from gconstants import *
import arcade
from time import time

class MouseHandler():
    """ Mouse Handler class for control of mouse and send result to InputHandler class """

    def __init__(self, input_h):
        """ MouseHandler constructor """
        self.input = input_h
        # List of elements sprits we are dragging with the mouse
        self.held_elements = []
        # Original location of cards we are dragging with the mouse in case
        # they have to go back for reset on ESC press
        self.held_elements_original_position = []
        self.button_name = [  "Left",
                              "Middle",
                              "Unknown",
                              "Right",
                              "Scroll Up",
                              "Scroll Down"]
        self.button_press_time = [  0,
                                    0,
                                    0,
                                    0,
                                    0,
                                    0]

    def set_on_mouse_press(self, x, y, button, key_modifiers, board):
        """ Called when the user presses a mouse button, get here from Board class call. """
        self.button_press_time[button-1] = time()
        # Get list of elements we've clicked on
        elements = arcade.get_sprites_at_point((x, y), board.elements_list)
        # Have we clicked on a element?
        if len(elements) > 0:
            self.on_pull(x, y, button, key_modifiers, elements[-1])
        else:
            return False

    def set_on_mouse_release(self, x: float, y: float, button: int,
                         key_modifiers: int, board):
        """ Called when the user presses a mouse button, get here from Board class call. """
        # If we don't have any elements, who cares
        if len(self.held_elements) == 0:
            return False
        # We are no longer holding elements
        # send each in list
        for element in self.held_elements:
            self.on_drop(x, y, button, key_modifiers, element)
            if time() - self.button_press_time[button-1] < TIME_FOR_CLICK:
                self.on_click(x, y, button, key_modifiers, element)

    def set_on_mouse_motion(self, x: float, y: float, dx: float, dy: float, board):
        """ User moves mouse, get here from Board class call.  """
        if len(self.held_elements) == 0:
            return False
        # If we are holding elements, move them with the mouse
        for element in self.held_elements:
            self.on_move(x, y, dx, dy, element)

    def on_left_release(self, x: float, y: float, button: int,
                         key_modifiers: int, element):
        """ Called when the user release a left mouse button. """
        self.input.handle_input("Left Relise", element, self,[x, y, button, key_modifiers])

    def on_click(self, x: float, y: float, button: int,
                         key_modifiers: int, element):
        """ Called when the user fast press and release a left mouse button. """
        self.input.handle_input(self.button_name[button-1] + " Click", element, self,[x, y, button, key_modifiers])

    def on_pull(self, x: float, y: float, button: int,
                         key_modifiers: int, element):
        """ Called when the user presses a mouse button. """
        self.input.handle_input("On "+ self.button_name[button-1] + " Pull", element , self, [x, y, button, key_modifiers])

    def on_drop(self, x: float, y: float, button: int,
                         key_modifiers: int, element):
        """ Called when the user release a element """
        self.input.handle_input("On "+ self.button_name[button-1] +" Drop", element, self, [x, y, button, key_modifiers])

    def on_move(self, x: float, y: float, dx: float, dy: float, element):
        """ Called when the user release a element """
        self.input.handle_input("On Move", element, self, [x, y, dx, dy])

    def setup(self):
        """ Called when the setup\reset the board. """
        # List of elements sprits we are dragging with the mouse
        self.held_elements = []
        # Original location of elements we are dragging with the mouse in case
        # they have to go back for reset on ESC press
        self.held_elements_original_position = []

    def add_to_held(self, element):
        self.held_elements.append(element)
        # Save the position
        self.held_elements_original_position.append(element.position)
        element.pull_to_top(element)

    def remove_from_held(self, element):
        i = self.held_elements.index(element)
        if not i ==-1: 
            self.held_elements.pop(i)
            # Save the position
            self.held_elements_original_position.pop(i)

    def on_left_double_clik(self, x, y, button, key_modifiers, element):
        """ Called when the user presses a mouse button fast twise. """
        pass

    def on_left_long_press(self, x, y, button, key_modifiers, element):
        """ Called when the user presses a mouse button more then 3 sec. """
        pass

if __name__ == "__main__":
    print("testin MouseHandler")
    from game import Game
    game = Game()
    from board import Board
    board = Board(game)
    test = MouseHandler("input")
    # element at these coordinates, because of this result is False
    assert(not test.set_on_mouse_release(1,2,3,4,board))
    assert(not test.set_on_mouse_press(1,2,3,4,board))
    assert(not test.set_on_mouse_motion(1,2,3,4,board))
    test.on_left_double_clik(1,2,3,4,"element")
