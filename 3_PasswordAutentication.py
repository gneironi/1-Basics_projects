#Password Authentication is the process of checking the identity of a user.
#Almost every online platform today makes sure that they only give access
#to the real user which can be only possible by asking for a password while
#a user wants to log in to the account.

#TODO: Create a Dictionary of users and passwords
#TODO: Ask for user input
#TODO: Use the getpass module


import getpass

database = {
    "german.neironi":"123456",
    "pablo.ruiz":"654321"
    }

username = input("Enter your username: ") 
password = getpass.getpass("Enter your password: ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Whrong password. Enter your password again: ")
        break
print("Verfified")

#Used tools:
#getpass library, dicts, input function, loop for and while
