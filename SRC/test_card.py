"""
p2tts2d game.
testing class 
2023-08-31
"""

import unittest
from card import *

class Test(unittest.TestCase):

    @classmethod 
    def setUpClass(self):
        class Board():
            def __init__(self):
                pass                                              

            def add_element(self, element):
                pass                                              

        keeper = Board()
        self.test = Card(keeper, "Clubs", "9",x=0,y=0)

    def test_init(self):
        self.assertIsNotNone( self.test.image_file_name_face_down )
        # self.assertEqual( self.test.texture, arcade.load_texture(self.test.image_file_name_face_down))
        self.assertEqual( self.test.events["event_flip"], self.test.face_flip)
        self.assertEqual( self.test.events["event_on_drop"], self.test.on_drop)

    def test_flip(self):
        self.assertFalse(self.test.is_face_up)              
        self.assertTrue(self.test.is_face_down)              
        self.test.face_flip("enput", "args")
        self.assertTrue(self.test.is_face_up)              
        self.assertFalse(self.test.is_face_down)              
        self.assertEqual( self.test.center_x, 0)

    def test_move(self):
        self.test.pulled = True
        args = [0,1,2,3]
        self.test.on_move("input",args)
        self.assertEqual( self.test.center_x, 2)
        self.test.on_move("input",args)
        self.assertEqual( self.test.center_x, 4)

if __name__ == "__main__":
    unittest.main()
