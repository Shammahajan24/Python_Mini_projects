import pwinput

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited RS.{amount}. New balance: RS.{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew RS.{amount}. New balance: RS.{self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance: RS.{self.balance}")


class ATMSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter a new 6-digit account number: ")
        if not account_number.isdigit() or len(account_number) != 6:
            print("Invalid account number! It must be a 6-digit number.")
            return
        if account_number in self.accounts:
            print("Account number already exists.")
            return
        
        pin = pwinput.pwinput("Create a 4-digit PIN: ", mask="*")  
        if not pin.isdigit() or len(pin) != 4:
            print("Invalid PIN! It must be a 4-digit number.")
            return
        
        self.accounts[account_number] = Account(account_number, pin)
        print("Account created successfully!")

    def login(self):
        account_number = input("Enter your account number: ")
        pin = pwinput.pwinput("Enter your PIN: ", mask="*")  
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            print("Login successful!")
            return account
        else:
            print("Invalid account number or PIN.")
            return None

    def run(self):
        while True:
            print("\n========================= Welcome to the ATM System ==========================")
            print("1. Create New Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                account = self.login()
                if account:
                    self.account_menu(account)
            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print(f"Invalid choise. There is no option for {choice} Please try again.")

    def account_menu(self, account):
        while True:
            print("\n====================== Account Menu =================================")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = self.get_valid_amount("Enter amount to deposit: ")
                if amount is not None:
                    account.deposit(amount)
            elif choice == "3":
                amount = self.get_valid_amount("Enter amount to withdraw: ")
                if amount is not None:
                    account.withdraw(amount)
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_valid_amount(self, prompt):
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return None
            return amount
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")
            return None

atm = ATMSystem()
atm.run()