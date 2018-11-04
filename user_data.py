import pyperclip
class User:
    details_list = []
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    def save_user(self):
        '''
        Saves new user details into details_list
        '''
        User.details_list.append(self)

    def delete_user(self):
        '''
        Deletes user profile from details_list
        '''
        User.details_list.remove(self)

    @classmethod
    def find_by_number(dls,number):
        '''
        Method that takes in a number and returns a user profile that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            User profile that matches the number.
        '''

        for user in dls.details_list:
            if user.phone_number == number:
                return user

    @classmethod
    def user_exist(dls, number):
         '''
        Method that checks if a user profile exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''

         for user in dls.details_list:
            if user.phone_number == number:
                    return True

                    return False



    @classmethod
    def display_users(dls):
        '''
        method that returns the users details list
        '''
        return dls.details_list
