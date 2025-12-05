#unit test file: main_test.py
import unittest
from agent import main

class main_challenges(unittest.TestCase):
    def test_default(self):
        self.assertEqual(1 + 1, 2)

    def test_my_first_pwnie(self):
        self.assertTrue(main("./main_challenges/my_first_pwnie"))

    def test_puffin(self):
        self.assertTrue(main("./main_challenges/puffin"))

    def test_target_practice(self):
        self.assertTrue(main("./main_challenges/target_practice"))

class extra_challenges(unittest.TestCase):
    def test_mooneys_bookstore(self):
        self.assertTrue(main("./extra_challenges/mooneys-bookstore"))
        


