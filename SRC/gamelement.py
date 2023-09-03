"""
p2tts2d game.
Game element class
2023-08-24
"""

from gconstants import *
import arcade

class Gamelement(arcade.Sprite):
    """ Game element sprite """

    def __init__(self, keeper,
                 image_file_name_face_up = None,
                 image_file_name_face_down = None,
                 scale=1, hit_box_algorithm="None"):
        """ Game element constructor """
        if not image_file_name_face_up:
            image_file_name_face_up = GAMELEMENT_FACE_UP_IMAGE
        if not image_file_name_face_down:
            image_file_name_face_down = GAMELEMENT_FACE_DOWN_IMAGE
        self.image_file_name_face_down = image_file_name_face_down
        self.image_file_name_face_up  = image_file_name_face_up
        self.is_face_up = True
        # Call the parent
        super().__init__(self.image_file_name_face_up, scale, hit_box_algorithm=hit_box_algorithm)
        self.add_to_keeper(keeper)
        self.pulled = False
        self.events = {"event_on_drop":self.on_drop,
                      "event_on_pull":self.on_pull,
                      "event_on_move":self.on_move}

    @property
    def is_face_down(self):
        """ Is this element ard face down? """
        return not self.is_face_up

    def face_down(self):
        """ Turn element face-down """
        self.texture = arcade.load_texture(self.image_file_name_face_down)
        self.is_face_up = False

    def face_up(self):
        """ Turn element face-up """
        self.texture = arcade.load_texture(self.image_file_name_face_up)
        self.is_face_up = True

    def face_flip(self, enput, args):
        """ Turn element to other side """
        if self.is_face_up:
            self.face_down()
        else:
            self.face_up()

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
