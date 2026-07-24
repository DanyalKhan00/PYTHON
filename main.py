import bank
balance = int(input("Enter the Balance :"))
print("1. Deposit")
print("2. withdraw")
print("3. Check balance")
choice = int(input("Enter Your Choice "))
if choice == 1:
    amount = float(input("Enter Deposit Amount "))
    balance = bank.deposit(balance,amount)
    print("Updated Balance :",balance)
elif choice == 2:
    amount = float(input("Enter Withdraw Amount "))
    balance = bank.withdraw(balance,amount)
    print("Updated Balance :",balance)
else:
    print("Invalid Choice ")
