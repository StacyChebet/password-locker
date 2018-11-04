import unittest
from user_data import User
import pyperclip

class TestUser(unittest.TestCase):
        def tearDown(self):
            '''
            Does clean up after each test has run
            '''
            User.details_list = []

        def setUp(self):
            '''
            Runs before each test case
            '''
            self.new_user = User(
            "Stacy", "Chebet", "0712345678", "staceychebet23@gmail.com", "12345")

        def test_init(self):
            '''
            tests if object is initialized correctly
            '''
            self.assertEqual(self.new_user.first_name, "Stacy")
            self.assertEqual(self.new_user.last_name, "Chebet")
            self.assertEqual(self.new_user.phone_number, "0712345678")
            self.assertEqual(self.new_user.email, "staceychebet23@gmail.com")
            self.assertEqual(self.new_user.password, "12345")

        def test_save_user(self):
            '''
            test if user object is saved in user_details
            '''
            self.new_user.save_user()
            self.assertEqual(len(User.details_list),1)

        def test_save_multiple_user(self):
            '''
            checks if it can save multiple user profiles
            '''
            self.new_user.save_user()
            test_user = User("Her", "Him", "0798765432", "himher@gmail.com", "01234")
            test_user.save_user()
            self.assertEqual(len(User.details_list),2)

        def test_delete_user(self):
            '''
            tests if it can remove a user profile from user_details
            '''
            self.new_user.save_user()
            test_user = User("Her", "Him", "0798765432", "himher@gmail.com", "01234")
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.details_list),1)

        def test_find_user_by_number(self):
            '''
            checks if it can find user by phone phone_number
            '''
            self.new_user.save_user()
            test_user = User("Her", "Him", "0798765432", "himher@gmail.com", "01234")
            test_user.save_user()

            found_user = User.find_by_number("0798765432")
            self.assertEqual(found_user.email, test_user.email)

        def test_user_exists(self):
            '''
            checks if user exists
            '''
            self.new_user.save_user()
            test_user = User("Her", "Him", "0798765432", "himher@gmail.com", "01234")
            test_user.save_user()

            user_exists = User.user_exist("0798765432")

            self.assertTrue(user_exists)

        def test_display_all_users(self):
            '''
            returns list of all saved users
            '''
            self.assertEqual(User.display_users(), User.details_list)

if __name__ == '__main__':
    unittest.main()
