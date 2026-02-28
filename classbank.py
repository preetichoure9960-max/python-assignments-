class bankaccount:
    def __init__(self, accountnumber, balance):
        self.accountnumber = accountnumber
        self.balance = balance
    def deposite(self):
        self.deposite=3400
        print(f"The deposite value is",self.deposite)
    def withdraw(self):
        self.withdraw=3000
        print(f"The withdraw value is",self.withdraw)
    def bankdetails(self):
        print(f"accountnumber:{self.accountnumber}")
        print(f"balance:{self.balance}")
bank1=bankaccount(250486709845,1000)
bank1.bankdetails()
bank1.deposite()
bank1.withdraw()

