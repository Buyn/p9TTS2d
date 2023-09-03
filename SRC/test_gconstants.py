"""
p2tts2d game.
testing setings 
2023-08-31
"""

import unittest
from gconstants import *

class Test(unittest.TestCase):

    def test_newText(self):
        test = CARD_SUITS
        self.assertIsNotNone( test )
        self.assertEqual( test[0], "Clubs")
        self.assertEqual( test[3], "Diamonds")
        test = TIME_FOR_CLICK

if __name__ == "__main__":
    unittest.main()
