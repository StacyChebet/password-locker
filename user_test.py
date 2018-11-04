import unittest
from user-data import User
import pyperclip

class TestUser(unittest.TestCase):
        def tearDown(self):
            '''
            Does clean up after each test has run
            '''
            User.details_list = []

        def SetUp(self):
            '''
            Runs before each test case
            '''
            self.new_user = User(
            "Stacy", "Chebet", "0712345678", "staceychebet23@gmail.com")
