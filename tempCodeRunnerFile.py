"""
ATM Machine simulation
-------------------
feature 
1. language selection(english, hindi)
2. pin verification
3.cash deposit
4.cash withdrawal
5. balance inquiry
6. exit/ card ejection
7. mini statement(last 5 transactions)
"""

import datetime

language = input("select the language: english or hindi: ")
if language == "english":
    pin = input("enter your pin: ")
    if pin == "1234":
        print("1. cash deposit")
        print("2. cash withdrawal")
        print("3. balance inquiry")
        print("4. mini statement")
        print("5. exit")
        option = int(input("select the option: "))
        if option == 1:
            amount = float(input("enter the amount to deposit: "))
            print(f"your amount {amount} is successfully deposited on {datetime.datetime.now()}")
        elif option == 2:
            amount = float(input("enter the amount to withdraw: "))
            print(f"your amount {amount} is successfully withdrawn on {datetime.datetime.now()}")
        elif option == 3:
            balance = 10000
            print(f"your balance is {balance} on {datetime.datetime.now()}")
        elif option == 4:
            print(f"your last transactions are: {datetime.datetime.now()}")
        elif option == 5:
            print("thank you for using our ATM machine. please take your card.")
        else:
            print("invalid option")
    else:
        print("invalid pin")
else:
    print("invalid language selection")





