
''' ************** Banking Mini Application Project **************'''
'''***** 4 classes used in this project ************'''
''' ******** Class one:Utility - Here, general utility methods are defined ********* '''
''' ******** Class two:Account - It is an abstract class. It consists of defined and undefined methods*****'''
''' ******** Class three:SavingsAccount - It is for defining bank menu options,balance enquiry and statements.'''
''' ******** Class three:CurrentAccount - It is for defining bank menu options,balance enquiry and statements.'''

from abc import *
from random import randint


class Utility:
    @staticmethod
    def GenerateAcountNo():
        Acct_No = ""
        for i in range(0, 9):
            Acct_No = Acct_No + str(randint(0, 9))
        return Acct_No

    @classmethod
    def Savings_Acct_Creation(cls):
        global Savings_Obj
        Name = input("Enter account holder name: ")
        Balance = eval(input("Enter the Balance amount: "))
        while Balance < 0:
            Balance = eval(input("Balance amount can't be negative. Please enter again: "))

        Savings_Obj = SavingsAccount(Name, Balance)
        print(Savings_Obj)
        Savings_Obj.Choices()

    @classmethod
    def Current_Acct_Creation(cls):
        global Current_Obj
        Organization = input("Enter your organization name: ")
        O_Balance = eval(input("Enter the Balance amount: "))
        while O_Balance < -1000:
            O_Balance = eval(input("Balance amount can't be less than -1000. Please enter again: "))

        Current_Obj = CurrentAccount(Organization, O_Balance)
        print(Current_Obj)
        Savings_Obj.Choices()

class Account(ABC):
    Bank_Name='IDB Bank'
    def __init__(self,Account_Holder_Name,Balance,Min_Balance):
        self.Account_Number=Utility.GenerateAcountNo()
        self.Account_Holder_Name=Account_Holder_Name
        self.Balance=Balance
        self.Min_Balance=Min_Balance

    @abstractmethod
    def Choices(self):
        pass

    def Withdraw(self):
        Amount = int(input("Enter withdraw amount: "))
        while Amount<=0 or Amount%100!=0:
            Amount = eval(input("Enter the correct amount to withdraw: "))

        if self.Balance-Amount >= self.Min_Balance:
            self.Balance-=Amount
            print("After withdraw, your",self.Account_Category,"balance is:",self.Balance)
        else:
            print("Your minimum balance is: ","Hence, you can't withdraw more than that.")

    def Deposit(self):
        Amount=int(input("Enter deposit amount: "))
        while Amount<=0:
            Amount = int(input("Invalid deposit amount. Please enter again: "))
        self.Balance+=Amount
        print("After deposit, your",self.Account_Category,"balance is:",self.Balance)

    @abstractmethod
    def BalanceInquiry(self):
        pass
    @abstractmethod
    def PrintAccountInfo(self):
        pass

class SavingsAccount(Account):
    def __init__(self,Name,Balance):
        super().__init__(Name,Balance,0)
        self.Account_Category="Savings"

    def __str__(self):
        return "Mr.%s,your account is created successfully. Account Number: %s. Account Category: %s" \
               %(self.Account_Holder_Name,self.Account_Number,self.Account_Category)

    def Choices(self):
        Choice_Count=1
        while True:
            if Choice_Count>1:
                Next_Round = input("Do you want to proceed again with bank menus ? Yes || No: ")
                if Next_Round.capitalize() == 'No':
                    break
            print("B - Balance Enquiry\n A - Account Information\n D - Deposit\n W - Withdrawl\n")
            Bank_Menu = input("Enter your choice to proceed: ")

            while Bank_Menu not in ['B', 'A', 'D', 'W']:
                Bank_Menu = input("Enter your choice again to proceed: ")
                print(" B - Balance Enquiry\nA - Account Information\nD - Deposit\nW - Withdrawl\n")

            if Bank_Menu == 'B':
                self.BalanceInquiry()
            elif Bank_Menu == 'A':
                self.PrintAccountInfo()
            elif Bank_Menu == 'D':
                self.Deposit()
            elif Bank_Menu == 'W':
                self.Withdraw()
            elif Choice_Count==4:
                break
            Choice_Count+=1

    def BalanceInquiry(self):
        print("Hello {},Balance in your Savings Account ends with xxxxxx{} is: {}".
              format(self.Account_Holder_Name,self.Account_Number[7:],self.Balance))

    def PrintAccountInfo(self):
        print("******Your Savings Account information*******")
        print("Account Number:",self.Account_Number)
        print("Customer Name:",self.Account_Holder_Name)
        print("Current Balance: ",self.Balance)


class CurrentAccount(Account):
    def __init__(self,Org,Bal):
        super().__init__(Org,Bal,-1000)
        self.Account_Category="Current"

    def __str__(self):
        return "The Account holder name is %s. Account Number: %s. Account Category: %s" \
               %(self.Account_Holder_Name,self.Account_Number,self.Account_Category)

    def Choices(self):
        Choice_Count = 1
        while True:
            if Choice_Count > 1:
                Next_Round = input("Do you want to proceed again with bank menus ? Yes || No: ")
                if Next_Round.capitalize() == 'No':
                    break
            print("B - Balance Enquiry\n A - Account Information\n D - Deposit\n W - Withdrawl\n")
            Bank_Menu = input("Enter your choice to proceed: ")

            while Bank_Menu not in ['B', 'A', 'D', 'W']:
                Bank_Menu = input("Enter your choice to proceed: ")
                print(" B - Balance Enquiry\nA - Account Information\nD - Deposit\nW - Withdrawl\n")

            if Bank_Menu == 'B':
                pass
            elif Bank_Menu == 'A':
                pass
            elif Bank_Menu == 'D':
                self.Deposit()
            elif Bank_Menu == 'W':
                self.Withdraw()
            elif Choice_Count==4:
                break
            Choice_Count+=1

    def BalanceInquiry(self):
        print("Hello {},Balance in your Current Account ends with xxxxxx{} is: {}".
              format(self.Account_Holder_Name,self.Account_Number[7:],self.Balance))

    def PrintAccountInfo(self):
        print("******Your Current Account information*******")
        print("Account Number:",self.Account_Number)
        print("Customer Name:",self.Account_Holder_Name)
        print("Current Balance: ",self.Balance)














