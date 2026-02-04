class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id, initial_balance=0):
        if account_id not in self.accounts:
            self.accounts[account_id] = initial_balance
            print(f"Account {account_id} created with balance ${initial_balance}")
        else:
            print(f"Account {account_id} already exists")
    
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id] += amount
            print(f"Deposited ${amount}. New balance: ${self.accounts[account_id]}")
        else:
            print(f"Account {account_id} not found")
    
    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            if self.accounts[account_id] >= amount:
                self.accounts[account_id] -= amount
                print(f"Withdrew ${amount}. New balance: ${self.accounts[account_id]}")
            else:
                print("Insufficient funds")
        else:
            print(f"Account {account_id} not found")
    
    def check_balance(self, account_id):
        if account_id in self.accounts:
            print(f"Balance: ${self.accounts[account_id]}")
        else:
            print(f"Account {account_id} not found")


if __name__ == "__main__":
    bank = Bank()
    bank.create_account("001", 1000)
    bank.deposit("001", 500)
    bank.check_balance("001")
    bank.withdraw("001", 200)
    bank.check_balance("001")