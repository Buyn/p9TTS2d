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
        # Call the parent
        super().__init__(image_file_name, scale, hit_box_algorithm=hit_box_algorithm)
        self.add_to_keeper(keeper)
        self.pulled = False
        self.events = {"on_drop":self.on_drop,
                      "on_pull":self.on_pull,
                      "on_move":self.on_move}
        # self.events = {"On Drop":self.on_drop,
        #               "On Pull":self.on_pull,
        #               "On Move":self.on_move}

    def add_to_keeper(self, new_keeper):
        self.keeper = new_keeper
        new_keeper.add_element(self)

    def on_move(self, enput, args):
        if self.pulled:
            # Perform action for the move event
            self.center_x += args[DX]
            self.center_y += args[DY]

    def on_pull(self, enput, args):
        if not self.pulled:
            # Perform action for the pull event
            self.pulled = True
            enput.add_to_held(self)
            self.keeper.pull_to_top(self)

    def on_drop(self, enput, args):
        if self.pulled:
            # Perform action for the pull event
            self.pulled = False
            # Attributes for suit and value
            enput.remove_from_held(self)

    def add_event(self, event, handler):
        self.events[event] = handler

    def remove_event(self, event):
        if event in self.events:
            self.events[event].pop(event)

    def pull_to_top(self, element: arcade.Sprite):
        """ Pull element sprite to top of rendering order (last to render, looks on-top) """
        # Remove, and append to the end
        self.keeper.pull_to_top(element)

    def move_to_keeper(self, new_keeper):
        """ Move elevent from curent keeper
to new one  """
        self.keeper.remove_element(self)
        self.keeper = new_keeper
        new_keeper.add_element(self)

if __name__ == "__main__":
    print("testin Gamelement")
    import game
    game = game.Game()
    import board
    board = board.Board(game)
    image_file_name = f":resources:images/cards/cardHeartsA.png"
    # CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]
    test = Gamelement(board, image_file_name)
    assert(test != None)
    # test.on_left_double_clik(1,2,3,4)
