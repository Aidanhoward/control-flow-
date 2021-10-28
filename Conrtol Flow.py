# programer: aidan howard
# Date: 10.11.2021
# program: ATM Bank Transaction

"""
this program simulates an ATM utilizing If, Elif, & Else statements
Nesting If statements and refresh our Comparison & Logical Operators
"""

print("Welcome to Cash-R-Us Bank\n\nLet's take a Moment to set up your account.\n")

# Set up account by asking users for their first & last names using Variables
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

print("\nWelcome to Cash-R-Us",first_name,last_name + ", we will now set up a security pin on your account.\n")

# set up a PIN - Personal Identification Number
pin = input("please choose a 4 digit Personal Identification Number: ")

print("\nThank you", first_name + ", we see that you set your PIN to",pin)

print("\nWould you like to make a transaction through our atuomated teller machine")
atm = input("Yes or No: ").upper()

if atm == "YES":
    print("\n*****************************************************\n")

    # this part of the program will be asking users to complete a transaction through the ATM
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM",first_name,last_name,"\n")
    user_pin = input("What is your four digit PIN:")

    if pin == user_pin:
        balance = 69420
        print("\nYour balance: $" + str(balance))
         # ask users what type of transaction they want - withdrawal - deposit
        type_of_transaction = input("\nWould you like to make a withdrawal or a deposit\nW = withdrawal - D = deposit: ").lower()
        if type_of_transaction == "w":
            withdrawal_amount = int(input("Enter amount of withdrawal:"))
            balance = balance - withdrawal_amount
            print("Your new balance is: $" + str(balance))
            
            

    else:
        print("\nSorry",first_name,last_name,"your PIN doesn't match our records")




else:
    print("\nHave a wonderful day", first_name,last_name +", please come back and visit soon.")
