import sys
from pythonProject.Banking.Banking_Project import *



print("\n******************Welcome to",Account.Bank_Name,"****************************")
print("Select the account you want to open/access: \n\t1.Savings Account\n\t2.Current Account")
Option=int(input("Enter the number that belongs to the account: "))

Count=1

while Option not in [1,2]:
    Count+=1
    Option = int(input("Please enter a valid option: "))
    if Count>2:
        print("You have exceeded max no of attempts to choose/access Account.Try after some time.Thanks!")
        sys.exit()

Operation=1
while Option in [1,2]:
    if Option==1:
        print("You chose Savings account.")
        Utility.Savings_Acct_Creation()
    elif Option==2:
        print("You chose Current account.")
        Utility.Current_Acct_Creation()
    Operation+=1
    Round = input("Next Round ?? ")
    if Round.capitalize()=='Yes' and Operation<=2:
        Option = int(input("Enter the number that belongs to the account: "))
    elif Round.capitalize()=='No' and Operation<=2:
        break
    elif Operation>2:
        print("Permitted no of accounts in this bank have been created. Thanks!")
        sys.exit()










