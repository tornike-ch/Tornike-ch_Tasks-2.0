
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    @property
    def get_balance(self):
        return self._balance

def main():    
    balance = BankAccount(2000)
    deposit = BankAccount.deposit(balance, 1000)
    withdraw = BankAccount.withdraw(balance, 500)
    print(balance.get_balance)


if __name__ == "__main__":
    main()