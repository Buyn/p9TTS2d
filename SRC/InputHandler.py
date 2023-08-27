"""
p2tts2d game.
Input Handler control Game class
2023-08-26
"""



class InputHandler():
    """ Input Handler class for get control of mouse and send event to elements """

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.inputs = {}

    def set_input(self, key, event):
        self.inputs[key] = event

    def handle_input(self, key, element, input, args=[]):
        if key in self.inputs:
            if self.inputs[key] in element.events:
                element.events[self.inputs[key]](input, args)

if __name__ == "__main__":
    print("testin InputHandler")
    test = InputHandler()
    test.set_input("1","2")
    import game
    game = game.Game()
    import board
    board = board.Board(game)
    image_file_name = f":resources:images/cards/cardHeartsA.png"
    # CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]
    import gamelement
    self = gamelement.Gamelement(board, image_file_name)
    events = {"On Drop":self.on_drop,
                      "On Pull":self.on_pull,
                      "On Move":self.on_move}
    tinput = game.input
    # tinput.handle_input("")
    # self.on_pull(x, y, button, key_modifiers, elements[-1])
    tinput.handle_input("On Pull", self , game.mouse, [1, 1, 1, 3])
    tinput.handle_input("On Move", self , game.mouse, [1, 1, 1, 3])
    # key = "On Pull"
    # if key in input.inputs:
    #     # print("handle_input key found",self.inputs[key], element.events )
    #     if input.inputs[key] in element.events:
    #         # print("handle_input send ", element.events[self.inputs[key]] )
    #         element.events[self.inputs[key]](input, args)
    # assert(test.set_input("1","2"), None)
    # test.on_left_double_clik(1,2,3,4)
