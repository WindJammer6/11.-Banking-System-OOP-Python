#About 'windy_banks.py' (the main program where the bank system is run): 

#Features:
#1. Allows user to choose to login or register an account, then re-logging in to their newly created 
#   account
#2. Login, with username and password clearance feature
#3. Types of transactions that are available once an user is logged in with their bank account:
#   -> Deposit
#   -> Withdrawal
#   -> Check balance

#These are official Python Libraries
import pandas as pd
import sys     #Just for the '.exit()' function to terminate the program whenever seems fit
import time    #Just for the '.sleep()' function for style points

#These are personal files imported from the same folder into this main file
from bank import UserDatabase
from user import User

#Loading the database in 2 different formats:
#1. As a dataframe, stored in the 'user_database' variable to be used in the 'name_login()' and 
#'password_login()' self-made function. (which is also why I need to make this variable global)

#2. As a list of objects in the 'database_user_list' variable to be used for easier manipulation of the 
#   account database such as during registration, deposit and withdrawal through the main code.
global user_database
user_database = pd.read_csv('account_database.csv')

database_object = UserDatabase('account_database.csv')
database_user_list = database_object.get_users()

def main():

    print('Welcome to Windy Banks!\n')


    #Code to get input if the user wishes to log in, or is a new user looking to register an account
    while True:
        try:
            login_or_register = input('Do you have an account or are looking to register an account? (Please enter the corresponding number)\n'
                                    '1. Log in\n'
                                    '2. Registration\n')
            if login_or_register == '1' or login_or_register == '2':
                break
            print('Please enter a valid option!')
        except:
            print('Please enter a valid option!')
    
    time.sleep(2)

    #If user wants to log in, this chunk of code is skipped to the log in portion of the code later.
    if login_or_register == '1':
        pass
    #If user wish to register, this chunk of code will run, and the user will be prompted to create an
    #account which will then be appended and re-saved/'updated' into the 'account_database.csv'
    else:
        database_user_list_updated = UserDatabase.registeration()
        df_registeration = pd.DataFrame([x.as_dict() for x in database_user_list_updated])
        df_registeration.to_csv('account_database.csv', index = False)
        print('Please rerun the program and log in to start making transactions!')
        sys.exit()

    #This is the log in page chunk of code, the user will be prompted for their registered bank account
    #name and password. Only if both inputs are correct and present, they will be logged in and connected
    #to their account and make transations with it
    print('This is the login page, please enter your name and password to login.')
    name = name_login()
    if name == 'exit':
        sys.exit()

    time.sleep(2)
    
    print(f'\nHello, {name}\n')

    password_login(name)
    
    time.sleep(2)
    
    #User has logged in
    print('You have successfully logged in!\n')

    time.sleep(2)

    #'Connecting' the user with their bank account by searching for the 'User' object in the list of
    #'User' objects with their self.name
    logged_in_user = next((obj for obj in database_user_list if obj.name == name), None)


    #This is where the main transactions occur, deposit, withdrawal, check balance or exit. Kept them in
    #a while loop so that in case multiple transactions needed to be made in 1 log in session and the
    #loop will only break if the user wishes to exit.
    running = True
    while running:
        while True:
            action = input(f'Welcome, {name}, what would you like to do today? (Please select the corresponding number)\n'
                '1. Deposit\n'
                '2. Withdraw\n'
                '3. View Balance\n'
                '4. Exit\n'
                )
            
            #Depending on what transaction is chosen, the corresponding transaction action's code
            #will be executed on their account in the database
            if action == '1':
                logged_in_user.deposit()
                break
            elif action == '2':
                logged_in_user.withdraw()
                break
            elif action == '3':
                logged_in_user.view_balance()
                break
            elif action == '4':
                print('Thank you for using Windy Banks services!')
                break
            print('Please enter a valid option!')

        if action == '4':
            break
        else:
            #This while loop is to check if the user made a valid input, as well as giving the user the
            #option to re-run through the main loop if they wish to make another transaction
            while True:
                try:
                    make_another_transaction = input('\nWould you like to make another transaction? (Please enter the corresponding number)\n'
                                                '1. Yes.\n'
                                                '2. No, please log me out.\n')
                    if make_another_transaction == '1' or make_another_transaction == '2':
                        break
                    print('Please enter a valid option!')
                except:
                    print('Please enter a valid option!')
            if make_another_transaction == '1':
                continue
            print('Thank you for using Windy Banks services!')
            break
    #After the corresponding transactions and the resulting changes made due to said transactions
    #on the dataframe (now in the format of a list of 'User' objects), the resulting list is then first
    #converted into the dictionary in '[x.as_dict() for x in database_user_list]', then back into a 
    #dataframe 'df' via pandas' 'pd.DataFrame()' function
    df = pd.DataFrame([x.as_dict() for x in database_user_list])

    #Can uncomment these to print out the changes in the dataframe and the list of objects after all
    #the transactions
    #   print(database_user_list[1].amount)
    #   print(df) #Can use this to check any update in database

    df.to_csv('account_database.csv', index = False)




#The 'name_login()' function. Checks in the dataframe's 'name' column for the inputed name of the user.
#If the name is present in the column it returns the inputed name as the identified logging in user, else
#the user has the option to terminate the program by entering 'exit' into the prompt
def name_login():
    x = list(user_database['name'])
    while True:
        try:
            name_input = str(input('Name: ')).lower()
            if name_input in x or name_input == 'exit':
                break
            print('This name does not have a bank account here! Please try again.\n'
                  '(If you wish to exit, please enter "exit")')
        except:
            print('This name does not have a bank account here!')
    return name_input

#The 'password_login()' function. Checks the same row in the 'password' column in the dataframe as in 
#the identified logging in user if the user put in the same password as the registered password of the
#account name. If it is then the user will be logged in and can proceed to the main transactions code
#in the main code.

def password_login(name):
    x = user_database.loc[user_database['name'] == name, 'password'].item()

    while True:
        try:
            password_input = str(input('Please enter the password: '))
            if password_input == x:
                break
            print('Incorrect password!')
        except:
            print('Incorrect password!')
    return True

main()