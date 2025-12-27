from random import randint

class BankAccount:
    def __init__(self, name, initial_balance):
        self.account_holder = name
        self.balance = float(initial_balance)
        self.account_number = randint(10000, 99999)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited PKR: {amount}. New Balance: PKR: {self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds!"
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            self.balance -= amount
            return f"Withdrawn PKR: {amount}. Remaining Balance: PKR: {self.balance}"

    def check_balance(self):
        return f"Current Balance: PKR: {self.balance}"

    def get_details(self):
        return f"Holder: {self.account_holder} | Acc #: {self.account_number}"

    @staticmethod
    def find_account(acc_num, bank_accounts):
        for account in bank_accounts:
            if str(account.account_number) == str(acc_num):
                return account
        return None
