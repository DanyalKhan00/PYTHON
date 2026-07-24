def deposit(balance,amount):
    balance = balance + amount
    return balance
def withdraw(balance , amount):
    if amount <= balance:
        balance = balance - amount
        return balance
def chk_bln(balance):
    return balance