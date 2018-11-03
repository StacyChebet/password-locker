import unittest
from user-data import User
import pyperclip

class TestUser(unittest.TestCase):
    def tearDown(self):
        User.details_list = []
