#About user.py:
#Contains code that executes any user-related operations when they are using the bank system such as 
#depositing, withdrawing and viewing their account balance.

#Some of the code are taken online or from ChatGPT

#Classes, Class Variables, Special Methods and its Instance/Class/Static methods:
#-> User Class, a Class that creates the user's account as an 'User' object

#-> '__init__' Special Method, that sets the attribute of the Class object, which is the user's name,
#   account password and amount they have in an account

#-> 'view_balance(self)' Instance Method, that basically prints and shows the user details of their
#   account such as their name and password. 

#-> 'withdraw(self)' Instance Method, which takes in an integer input of the amount of money that the user
#   wants to withdraw from their bank account and then subtracts said amount from their bank account.

#-> 'deposit(self)' Instance Method, which also takes in an integer input of the amount of money that the
#   user wants to add into their bank account. The method then updates that amount.

#-> 'as_dict(self)' Instance Method (obtained from ChatGPT, with slight modifications to fit my code's
#   purpose), which converts the list of 'User' objects into a dicitionary with the same column names as
#   the initial database. This dictionary will then run through pandas' 'pd.DataFrame()' function to
#   convert the dictionary into a dataframe to be re-saved back into the same database, effectively
#   updating the database.


#The User class
class User:

    #The __init__ Special Method
    def __init__(self, name, password, amount):
        self.name = name
        self.password = password
        self.amount = amount

    #The view_balance(self) Instance Method
    def view_balance(self):
        print('Here are your account details.\n')
        print('Account name:', self.name, '\nAccount balance:', self.amount)
        print('')

    #The withdraw(self) Instance Method. Added extra rules (not just simply subtracting intial amount
    #with withdrawn amount). 
     
    #If the account has not enough money, aka initial amount < withdrawn amount the transaction will not 
    #go through.

    #For security purposes, withdrawn amount per transaction is capped at $1000, to prevent sudden 
    #withdrawal for a large sum of money. If more than $1000 is entered, the transaction will also
    #not go through.

    #Returns with a notifier that the transaction has been successful, showing amount withdrawn and
    #amount left.
    def withdraw(self):
        while True:
            try:
                money_to_withdraw = int(input('How much would you like to withdraw (max $1000): '))
                if money_to_withdraw <= self.amount and money_to_withdraw <= 1000:
                    self.amount = self.amount - money_to_withdraw
                    break
                elif money_to_withdraw > self.amount:
                    print('Insufficient funds!')
                elif money_to_withdraw > 1000:
                    print('We only accept up to $1000 withdrawal per transaction.')
            except:
                print('There has been an error.')
        print(f'Transaction successful. Thank you for using Windy Banks, you have withdrawn ${money_to_withdraw}, and have ${self.amount} left in your account\n')
        return self.amount
    
    #The deposit(self) Instance Method. More clear cut and less rule than withdraw(self), as there is no
    #limit to how much the users can add into their account at once. Works by updating the initial amount
    #with total = initial amount + deposited amount

    #Returns with a notifier that the transaction has been successful, showing amount deposited and
    #amount left.

    def deposit(self):
        money_to_deposit = int(input('How much would you like to deposit: '))

        self.amount = self.amount + money_to_deposit
        
        print(f'Transaction successful. Thank you for using Windy Banks, you have deposited ${money_to_deposit}, and now have ${self.amount} in your account\n')
        return self.amount
    
    #The as_dict(self) Instance Method. When run as a catalyst in a for loop that iterates through the
    #'User' object list, it converts each 'User' object in the list of 'User' objects into a dictionary 
    #and returns said dictionary, with the self.name attributes of each 'User' object in the list being
    #classified under the 'name' column, the self.password attributes being classified as the 'password'
    #column and the self.amount attributes being classified as the 'amount' column (hence now effectively
    #a dataframe-in-dictionary format instead of a list of 'User' object format)
    def as_dict(self):
        return {'name': self.name, 'password': self.password, 'amount': self.amount}
    




