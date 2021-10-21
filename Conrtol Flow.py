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

print("\nThamk you", first_name + ", we see that you set your PIN to",pin)

print("\nWould you like to make a transaction thriugh our atuomated teller machine")