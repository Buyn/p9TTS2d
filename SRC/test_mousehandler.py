"""
p2tts2d game.
testing class 
2023-09-01
"""

import unittest
from mousehandler import *
from unittest.mock import patch
import time

class Arcade ():
  def __init__(self):
      self.mesage = []
      self.elements_list = []

  def get_sprites_at_point(self, point, elements_list):
      return ["element"]

arcade = Arcade()

class Test(unittest.TestCase):

      @classmethod 
      def setUpClass(self):
          class Board():
            def __init__(self):
                self.mesage = []
                self.elements_list = []

            def handle_input(self, key, element, input, args=[]):
                self.mesage.append(key)

          class Input():
            def __init__(self):
                self.mesage = []

            def handle_input(self, key, element, input, args=[]):
                self.mesage.append(key)

          self.board = Board() 
          self.input = Input()
          self.test = MouseHandler(self.input)

      def test_init(self):
          self.assertEqual( self.test.button_name[LEFT_CLICK-1], "Left")
          self.assertEqual( self.test.button_press_time[LEFT_CLICK-1], 0)

      @patch('arcade.get_sprites_at_point')  # Заменяем функцию 
      def test_left_click(self, get_sprites_at_point):
          get_sprites_at_point.return_value = ["elemet"]  # Задаем, что должно вернуться при вызове mock_function
          self.assertEqual( self.test.button_press_time[LEFT_CLICK-1], 0)
          self.test.set_on_mouse_press(0, 0, LEFT_CLICK, 0, self.board)
          self.assertEqual( self.test.input.mesage.pop(), "On Left Pull")
          self.assertNotEqual( self.test.button_press_time[LEFT_CLICK-1], 0)
          time.sleep(0.0001)
          self.assertNotEqual( self.test.button_press_time[LEFT_CLICK-1], 0)
          self.test.held_elements=["element"]
          self.test.set_on_mouse_release(0, 0, LEFT_CLICK, 0, self.board)
          self.assertEqual( self.test.input.mesage.pop(), "Left Click")

      def test_move(self):
          self.test.held_elements=["element"]
          self.test.set_on_mouse_motion(0, 0, 0, 0, "element")
          self.assertEqual( self.test.input.mesage.pop(), "On Move")

      @patch('arcade.get_sprites_at_point')  # Заменяем функцию 
      def test_on_drop(self, get_sprites_at_point):
          self.test.input.mesage = []
          self.test.button_press_time[LEFT_CLICK-1] = time.time()
          get_sprites_at_point.return_value = ["elemet"]  # Задаем, что должно вернуться при вызове mock_function
          self.test.held_elements=["element"]
          self.test.set_on_mouse_release(0, 0, LEFT_CLICK, 0, self.board)
          # print(self.test.input.mesage)
          self.assertEqual( len(self.test.input.mesage), 2)
          self.assertEqual( self.test.input.mesage.pop(), "Left Click")
          self.assertEqual( self.test.input.mesage.pop(), "On Left Drop")

if __name__ == "__main__":
    unittest.main()
