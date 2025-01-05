class customer:
    def __init__(self,name,age,bankname,contact_no,balance,task):
        self.name=name
        self.age=age
        self.b_name=bankname
        self.no=contact_no
        self.balance=balance
        self.task=task
         
    def method(self):
        if self.task==2:
            amount=int(input("Enter The Deposite amount:"))
            total=balance+amount
            print("Your Total balance is",total)
        elif self.task==1:
            amount=int(input("Enter The Withdrawl amount:"))
            total=balance-amount
            print("Your Total balance is",total)
        else:
            print("Try Again!!!")    

name=input("Enter the name :")
age=int(input("Enter the age of customer:"))
bankname=input("Enter the bank name:")
contact_no=int(input("contact number:"))
balance=int(input('total balance:'))
task=int(input("Select the option Number :- 1.Withdraw / 2.Deposite :"))

t=customer(name,age,bankname,contact_no,balance,task)
t.method()


