"""
p2tts2d game.
setings file
"""

import arcade

# Screen title and size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "p9TableTop 2D Board"

BOARD_BACKGROUND_COLOR = arcade.color.AMAZON

# Constants for sizing
CARD_SCALE = 0.6

# How big are the cards?
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

# Card constants
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_JOKER = f":resources:images/cards/cardJoker.png"
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]

# If we fan out cards stacked on each other, how far apart to fan them?
CARD_VERTICAL_OFFSET = CARD_HEIGHT * CARD_SCALE * 0.3

# gamelement image
GAMELEMENT_FACE_UP_IMAGE = ":resources:images/items/gemBlue.png"
GAMELEMENT_FACE_DOWN_IMAGE = ":resources:images/items/gemRed.png"
# Face down image
CARD_FACE_DOWN_IMAGE = ":resources:images/cards/cardBack_blue2.png"

# mouse motion constants
X   = 0
Y   = 1
DX  = 2
DY  = 3

# event.button integer values:
LEFT_CLICK   = 1
MIDDLE_CLICK = 2
UNNOWN_MOUSE_CLICK = 3
RIGHT_CLICK  = 4 
SCROLL_UP    = 5
SCROLL_DOWN  = 6

# mouse setings 
TIME_FOR_CLICK = 0.1
TIME_FOR_LONG_PRESS = 2

# How big is the mat we'll place the card on?
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

# How much space do we leave as a gap between the mats?
# Done as a percent of the mat size.
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

# The Y of the bottom row (2 piles)
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The X of where to start putting things on the left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

# The Y of the top row (4 piles)
TOP_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The Y of the middle row (7 piles)
MIDDLE_Y = TOP_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# How far apart each pile goes
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

if __name__ == "__main__":
    print("testin Game constants")
    test = X
    assert(test == 0)
    # test.on_left_double_clik(1,2,3,4)
