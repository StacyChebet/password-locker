import pyperclip
class User:
    details-list = []
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    def save_details(self):
        User.details_list.append(self)
