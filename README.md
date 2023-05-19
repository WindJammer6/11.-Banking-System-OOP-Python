# 11.-Banking-System-OOP-Python :bank::desktop_computer:
A personal project to simulate how a banking system would be created (a bit like how an ATM machine works).

## Thoughts on starting this project
My ninth programming project, in Python. Though it did not take me very long to create it due to many already available sources of similar banking system projects already being created and that I had ample practice with Object Oriented Programming (OOP) in Python prior to making this project. After completing the OOP learning journey in '
10.-Object-Oriented-Programming-OOP-Learning-and-Practice-Python', I thought that similarly to how I did 2 data analysis projects after completing the NumPy, Pandas and Matplotlib learning journey to really put I have learnt to the test, I decided to also work on an OOP-related project and after searching, I stumbled on a list of OOP Python project ideas (I'll attach the link below) and decided to go for creating of a Bank System using OOP in Python.

I also had various sources and making use of the power of AI (ChatGPT) in the process to help me kickstart such as finding out what kind of features that I am able to add into my banking system OOP project and to overcome struggles I have faced getting the logic of my code right.

This is my first time I had a personal project that required importing from other Python files (where the self-made OOP Classes are stored) to the main Python file where the main Python program is (in the same directory) to keep the code look tidy and not all cramped together, so thats cool 😄. I've seen it a couple of times, but never knew whats going on when programmers transition between Python files on a single project when they do coding up till now.

<br>

Sources:

https://copyassignment.com/python-oop-projects-source-code-and-example/ (OOP Python project ideas) 

https://www.youtube.com/watch?v=xTh-ln2XhgU (Johan Gondinho)                                                                                                                
(Idea for Banking System features of deposit, withdraw  and view balance came from here. However, I thought his program could have been more realistic by adding a database so that the program will actually remember user accounts)

https://github.com/bizarrenebula/Simple-Banking-System (bizarrenebula on Github)                                                                                         
(Idea for Banking System feature of user registration and a database to store the user's account information, changing in real time when transactions are made and retrive the account info when needed)

https://openai.com/blog/chatgpt (ChatGPT)

<br>

Computer program used for coding: VS Code

## Table of Contents <a name = "codedescription"></a>
+ [Code Description](#codedescription)
   1. [Banking System Features](#bankingsystemfeatures)
   2. [Bank-related operations (bank.py)](#bankrelatedoperations)
   3. [User-related operations (user.py)](#userrelatedoperations)
   4. [Bank Database (account_database.csv)](#bankdatabase)
   5. [Windy Banks (windy_banks.py)](#windybanks)
+ [Output](#output)
   1. [Registration](#registration)
   2. [Login and Running Transactions](#loginandrunningtransactions)
+ [Thoughts after the project](#thoughts)

<br>

<br>

## Code Description <a name = "codedescription"></a>

### 1. Banking System Features <a name = "bankingsystemfeatures"></a>

Here's a summary of what my version of the Banking System does:

1. Allows user to choose to login or register an account, then they can re-run the program to login to their newly created account

2. Login, with username and password clearance feature

3. Types of transactions that are available once an user is logged in with their bank account:  
   -> Deposit  
   -> Withdrawal  
   -> View balance
   
<br>
   
<br>

### 2. Bank-related operations (bank.py) <a name = "bankrelatedoperations"></a>

This file contains code that executes any administrative operations within the bank system such as user registration and loading of the database into the code.

Classes, Class Variables, Special Methods and its Instance/Class/Static methods in 'bank.py':  
1. 'UserDatabase' Class 

2. '__init__' Special Method, sets the attribute of the Class object, which is just the loaded csv bank account database file that we will be manipulating 

3. 'get_users(self)' Instance Method, (obtained from ChatGPT, with slight modifications to fit my code's purpose) converts the loaded database in the main 'windy_banks.py' file into a list (stored as the 'users' Class variable) of 'User' objects that we can efficiently work with when running transactions within the bank (we can see this in the main 'windy_banks.py' file)

4. 'registeration()' Static Method

5. 'users' Class variable, which is a variable that will store the loaded database from 
   'account_database.csv' as a list of 'User' objects via the 'get_users(self)' Instance Method.
   
More technical details is provided as comments within the code itself.
   
<br>

<br>

### 3. User-related operations (user.py) <a name = "userrelatedoperations"></a>

This file contains code that executes any user-related operations when they are using the bank system such as depositing, withdrawing and viewing their account balance.

Classes, Class Variables, Special Methods and its Instance/Class/Static methods in 'user.py':  
1. 'User' Class

2. '__init__' Special Method, sets the attribute of the Class object, which is the user's name, account password and amount they have in an account

3. 'view_balance(self)' Instance Method

4. 'withdraw(self)' Instance Method

5. 'deposit(self)' Instance Method

6. 'as_dict(self)' Instance Method (obtained from ChatGPT, with slight modifications to fit my code's purpose), which converts the list of 'User' objects into a dicitionary with the same column names as the initial database. This dictionary will then run through pandas' 'pd.DataFrame()' function to convert the dictionary into a dataframe to be re-saved back into the same database, effectively updating the database.

More technical details is provided as comments within the code itself.

<br>

<br>

### 4. Bank Database (account_database.csv) <a name = "bankdatabase"></a>
```
name,password,amount
john,john66,10000
mary,m@ry23,22500
tim,timmy8989,50000
jacob,windyhammer,30000
susan,suziesusan,39000
thebest,thebest,10000000000000000
james,jamesbond,1
windjammer,breezerestricter,0
```
A look into the database at the time of posting this repository into Github.

This file stores all the accounts that have already been registered into Windy Banks and will be able to login into the Bank System. Whenever a new account is registered, the database will be appended and store this new account in the lowest row.

<br>

<br>

### 5. Windy Banks (windy_banks.py) <a name = "windybanks"></a>

This file contains code that runs the main banking system program, importing functionality of the Classes from 'bank.py' and 'user'py' for it to work.

Python libraries imported:  
```python
import pandas as pd
import sys
import time  
```
1. Pandas, to load the database into 'windy_banks.py'
2. sys, for the 'exit()' function to terminate my program whenever its needed to
3. time, for the 'sleep()' function to make the program more user-friendly 

Important variables and functions in 'windy_banks.py':  
1.
```python
global user_database
user_database = pd.read_csv('account_database.csv')
```
'user_database' variable that stores the loaded csv file as a dataframe to be used (due to the nature of how my 'name_login()' and 'password_login()' functions are constructed to scan a dataframe for the name and password respectively instead of a list of 'User' objects (see below)) 

2.
```python
database_object = UserDatabase('account_database.csv')
database_user_list = database_object.get_users()
```
'database_user_list' variable also stores the loaded csv, but instead of as a dataframe, it stores as it as a list of 'User' objects for easy manipulation in the main code

3. 'main()', the main code

4. 'name_login()' self-made function

5. 'password_login()' self-made function

More technical details is provided as comments within the code itself.

Something I would like to point out is about the way the database is able to work with my program. I first had to convert the dataframe in 'account_database.csv' to a list of 'User' object via 'get_users(self)', where changes (withdrawal/deposit/registration) are made to this list, and then to save the changes back into the 'account_database.csv' file, I had to, at the end of the transations, convert the list first to a dictionary via 'as_dict(self)', then back to a dataframe via panda's 'pd.DataFrame()' function to be reuploaded back into the same csv file.

<br>

<br>

## Output (the exciting part):grinning: <a name = "output"></a>

Note that this output is obtained by running the 'windy_banks.py' file

### Registration: <a name = "registration"></a>
```
Welcome to Windy Banks!

Do you have an account or are looking to register an account? (Please enter the corresponding number)
1. Log in
2. Registration
34
Please enter a valid option!
Do you have an account or are looking to register an account? (Please enter the corresponding number)
1. Log in
2. Registration
2
We will need some of your personal information to set up an account for you.
Please enter the name you want for the account: thomas
Please set your password (must be at least 7 characters): 99     
Please set your password with at least 7 characters!
Please set your password (must be at least 7 characters): 995555
Please set your password with at least 7 characters!
Please set your password (must be at least 7 characters): thomaswayne99
Your account have been successfully created!

Account name: thomas
Password: thomaswayne99
Amount: $0

Please rerun the program and log in to start making transactions!
```
Notice that the user typed in invalid inputs (at login/register part and setting of password part) and is re-prompted again. Once the account is set, it is added into the 'account_database.csv' database and the user is automatically logged out and will need to rerun the program to login to their newly made account.

```
name,password,amount
john,john66,10000
mary,m@ry23,22500
tim,timmy8989,50000
jacob,windyhammer,30000
susan,suziesusan,39000
thebest,thebest,10000000000000000
james,jamesbond,1
windjammer,breezerestricter,0
thomas,thomaswayne99,0
```
Here's a look at the database. Compared to in '4. Bank Database (account_database.csv)', Thomas' account was not present before. Also note that the amount in his account is set at $0 by default when his account was created.

<br>

### Login and Running Transactions: <a name = "loginandrunningtransactions"></a>
```
Welcome to Windy Banks!

Do you have an account or are looking to register an account? (Please enter the corresponding number)
1. Log in
2. Registration
1
This is the login page, please enter your name and password to login.
Name: thoma 
This name does not have a bank account here! Please try again.
(If you wish to exit, please enter "exit")
Name: thomas 

Hello, thomas

Please enter the password: thomaswayne
Incorrect password!
Please enter the password: thomaswayne99
You have successfully logged in!

Welcome, thomas, what would you like to do today? (Please select the corresponding number)
1. Deposit
2. Withdraw
3. View Balance
4. Exit
1
How much would you like to deposit: 2000
Transaction successful. Thank you for using Windy Banks, you have deposited $2000, and now have $2000 in your account


Would you like to make another transaction? (Please enter the corresponding number)
1. Yes.
2. No, please log me out.
1
Welcome, thomas, what would you like to do today? (Please select the corresponding number)
1. Deposit
2. Withdraw
3. View Balance
4. Exit
2
How much would you like to withdraw (max $1000): 10000
Insufficient funds!
How much would you like to withdraw (max $1000): 1000
Transaction successful. Thank you for using Windy Banks, you have withdrawn $1000, and have $1000 left in your account

Would you like to make another transaction? (Please enter the corresponding number)
1. Yes.
2. No, please log me out.
2
Thank you for using Windy Banks services!
```
Notice that in this run, the user also made some invalid inputs (at wrong password/name/withdrawing too much money part) and is re-prompted again. It is not possible to show here, but I also added 'time.sleep(2)' in the code at relevant places to make the program seem more user-friendly and not show an output immediately once the user hits enter which may confuse the user.

```
name,password,amount
john,john66,10000
mary,m@ry23,22500
tim,timmy8989,50000
jacob,windyhammer,30000
susan,suziesusan,39000
thebest,thebest,10000000000000000
james,jamesbond,1
windjammer,breezerestricter,0
thomas,thomaswayne99,1000
```
Here's a look at the database again. From the above run, Thomas initially had $0 in his bank account, then he deposited $2000, then withdraw $1000 in 2 seperate transaction in the same run of the program. Hence the resulting amount in his account should be $1000 in his account which is shown to be in True in the database.

<br>

<br>

## Thoughts after the project <a name = "thoughts"></a>

I faced many unique challenges when implementing this Banking System. Here are the more significant challenges I faced:

-When it came to implementing a database into my project. (I believe when it comes to databases, the SQL Language is used, but for this project I had to improvise based on my current knowledge) This gave rise of many cryptic-looking functions being created with the help of ChatGPT (and some modifications to suit my code's purpose) such as 'as_dict(self)' and 'get_users(self)' to tackle the problem.

-Getting the multiple Classes to work together and having to refer consistently between the 3 files, 'windy_banks.py' (where the main bank system is), 'user.py' (where the 'User' Class is) and 'bank.py' (where the 'UserDataBase' Class is) to get the coding logic to work

-Setting up the 'name_login()' and 'password_login()' functions and learning how to get them to scan the dataframe for an account being already present/registered in the dataframe and checking if the password thee user input is the registered password before they are logged in

-I made this Banking System with the idea of it being as user-friendly as possible and with it comes with styling with 'time.sleep()' and making sure false inputs are well handled by the program to not show any cryptic messages. This forced me to create a lot of loops (such as allowing multiple transactions to be able to take place in a single run of the program using multiple while loops) and it was a challenge to check the flow of the loops by entering correct/expected inputs as well as intentionally trying to crash my program to detect any bugs by providing unexpected inputs so that I can patch them up.

<br>

Have a gif:

![Semantic description of image](https://media4.giphy.com/media/GeimqsH0TLDt4tScGw/200w.webp?cid=ecf05e47qay4jqawe7nw3xpt76cn1n2qu1va8rld7g3h5g17&ep=v1_gifs_search&rid=200w.webp&ct=g)
