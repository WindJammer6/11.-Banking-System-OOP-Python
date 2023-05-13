#About bank.py:
#Contains code that executes any administrative operations within the bank system such as user 
#registration and loading of the database into the code.

#Some of the code are taken online or from ChatGPT

#Classes, Class Variables, Special Methods and its Instance/Class/Static methods:
#-> UserDatabase Class, a Class that deals with the user account database such as loading of the bank's 
#   user database ('account_database.csv') into the bank system and new account registrations being added
#    into the database

#-> '__init__' Special Method, that sets the attribute of the Class object, which is just the loaded
#   csv bank account database file that we will be manipulating 

#-> 'get_users(self)' Instance Method (obtained from ChatGPT, with slight modifications to fit my code's
#   purpose), converts the loaded database (in the main 'windy_banks.py' file into a list (stored as the 
#   'users' Class variable) of 'User' objects that we can efficiently work with when running transactions
#   within the bank (we can see this in the main 'windy_banks.py' file)

#-> 'registeration()' Static Method, gets the details of new users looking to register into the bank by
#   obtaining their personal information such as name and chosen password and creating as well as 
#   uploading these information as an account into the user database (by first adding them to the 'users'
#   list, which will then be converted to a dictionary, then a dataframe, and then stored back into the
#   same 'account_database.csv' file, effectively 'uploading' the database with this new account, but 
#   this is set to be executed in the main code instead of this seperate 'bank.py' file)

#-> 'users' Class variable, which is a variable that will store the loaded database from 
#   'account_database.csv' as a list of 'User' objects via the 'get_users(self)' Instance Method.

import pandas as pd
#Just to add the '.sleep()' function to make the program more user-friendly
import time

#Required to import the 'User' class object so to create the 'get_users(self)' function which converts
#the account database into a list of 'User' objects
from user import User

#The 'users' Class variable, storing all the account database information in the form of a list for easy
#manipulation of their data in the main file. This list will then be converted to dictionary, then
#dataframe and re-uploaded into the same csv file in the main code, effectively updating the database
#when any transaction/registration is done.
users = []

#The UserDataBase Class
class UserDatabase:

    #The __init__ Special Method
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    #The get_users(self) Instance Method (obtained from ChatGPT)
    #I was struggling alot on trying to figure how on earth do I convert a dataframe into my 'Users' 
    #object by rows. Consulted ChatGPT and this is how it did it, via iterating through each row and
    #setting each element per row, depending their column as an attribute of my 'User' object.
    
    #My database is split into the 'name', 'password' and 'amount' columns, which are what I also what
    #I have set my 'User' object attributes as. Hence the code below is able to iterate through the
    #database and create an 'User' object for every row of my database, and storing them into the 'users'
    #Class variable
    def get_users(self):
        for index, row in self.data.iterrows():
            user = User(row['name'], row['password'], row['amount'])
            users.append(user)
        return users
    
    #The registration() Static Method. Gets new user's name, and prompting for a password set. To make
    #sure their password is somewhat decently strong, they must be minimumly 7 characters long and not
    #just single characters like 'a' or 'b'. (I believe real life password prompts will definitely ask
    #for more niche inputs like minimum 2 numbers, and at least 1 special letter, but I decidedly to
    #keep my password simple for the sake of the focus of this project being for OOP instead)

    #Once the inputs are given, this method then creates an 'User' object from the given information,
    #with $0 as the default amount, into the 'users' Class variable.
    @staticmethod
    def registeration():
        print('We will need some of your personal information to set up an account for you.')
        name_of_person = str(input('Please enter the name you want for the account: '))
        while True:
            try:
                password_set = str(input('Please set your password (must be at least 7 characters): '))
                if len(password_set) > 6:
                    break
                print('Please set your password with at least 7 characters!')
            except:
                print('Please set your password with at least 7 characters!')
        
        user = User(name_of_person, password_set, 0)
        users.append(user)

        time.sleep(2)
        print('Your account have been successfully created!\n\n'
              f'Account name: {name_of_person}\n'
              f'Password: {password_set}\n'
              f'Amount: $0\n')
        time.sleep(2)
        return users
        
#Testing zone, to test if specific parts of the above code works. 'if __name__ == '__main__':' helps to 
#show clearly this code only runs when I run this file and not run when I run other files with this file 
#imported to 
if __name__ == '__main__':
    database_object = UserDatabase('account_database.csv')
    database_user_list = database_object.get_users()
    print(database_user_list[1].password)