import unittest
from user_data import User
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

        def test_init(self):
            '''
            tests if object is initialized correctly
            '''
            self.assertEqual(self.new_user.first_name, "Stacy")
            self.assertEqual(self.new_user.last_name, "Chebet")
            self.assertEqual(self.new_user.phone_number, "0712345678")
            self.assertEqual(self.new_user.email, "staceychebet23@gmail.com")
