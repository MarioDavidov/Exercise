class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            print(f'User with {user.user_id} already registered in the library!')

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
        else:
            print(f'We could not found such user {user.username} to remove')

    def change_username(self, user_id: int, new_username: str):
        user_for_renaming = [x for x in self.user_records if x.user_id == user_id]

        if user_for_renaming:
            if user_for_renaming[0].username == new_username:
                print('Please chek again the provided username, it should be different than the username used so far!')
            else:
                user_for_renaming[0].username = new_username
                print(f'Username successfully changed to {new_username} for user id = {user_id}')
        else:
            print(f'There is not user with user id = {user_id}')
