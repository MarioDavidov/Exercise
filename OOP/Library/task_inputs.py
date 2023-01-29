from OOP.Library.Library import Library
from OOP.Library.User import User

user = User(12, 'Peter')
Testing_message_remove_user = User(1, "Mario")
library = Library()
library.add_user(user)
print(library.add_user(user))
print(library.remove_user(Testing_message_remove_user))
library.change_username(15, 'Peter')
library.change_username(12, 'Peter')
library.change_username(12, 'Brand new Petar')
print(user.username)

