class BankAccount:
    bank_name = 'Liberation Cooperative'
    all_accounts = []

    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_acct_balance(self):
        return f"Balance: ${round(self.balance, 2)}\n"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate

    @classmethod
    def all_balances(cls):
        for acct in cls.all_accounts:
            print(BankAccount.display_acct_balance(acct))

    @classmethod
    def all_info(cls):
        acct_num = 1
        for acct in cls.all_accounts:
            print(
                f"{cls.bank_name}\nacct_{acct_num}:\n{BankAccount.display_acct_balance(acct)}")
            acct_num += 1


acct_1 = BankAccount(.005, 300)
acct_2 = BankAccount(.0055, 1000)

acct_1.deposit(457.32).deposit(469.77).deposit(
    471.11).withdraw(253.13).yield_interest()
print(acct_1.display_acct_balance())

acct_2.deposit(559.91).deposit(532.91).withdraw(157.12).withdraw(
    37.13).withdraw(129-47).withdraw(27.53).yield_interest()
print(acct_2.display_acct_balance())

BankAccount.all_info()
