
import random

class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = random.randint(100000, 999999)
        print(f"\nAccount created for {self.account_holder} (A/c No: {self.account_number}) with ${self.balance:.2f}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("\nInvalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print(f"\nInvalid amount or insufficient funds! Balance: ${self.balance:.2f}.")

    def display(self):
        print(f"\nAccount Holder: {self.account_holder} | Account No: {self.account_number} | Balance: ${self.balance:.2f}")
if __name__ == "__main__":
    name = input("Enter account holder's name: ")
    initial_deposit = float(input("Enter initial deposit amount: $"))
    user_account = BankAccount(name, initial_deposit)

    while True:
        print("\n1. Deposit | 2. Withdraw | 3. Display | 4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            user_account.deposit(float(input("Deposit amount: $")))
        elif choice == '2':
            user_account.withdraw(float(input("Withdraw amount: $")))
        elif choice == '3':
            user_account.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")