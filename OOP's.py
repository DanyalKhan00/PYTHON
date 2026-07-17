#************ ALL ABOUT CLASS AND OBJECT ***********


#Q1: BANK ACCOUNT SYSTEM.........

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit Successful")
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal Successful")
#         else:
#             print("Insufficient Balance")
#     def show_balance(self):
#         print("Current Balance =", self.balance)
# b = BankAccount("Ahmed",5000)
# b.deposit(1000)
# b.withdraw(3000)
# b.show_balance()


#Q2:  EMPLOYEE SALARY ...

# class Emp:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def gross_salary(self):
#         hra= self.salary * 0.20
#         da = self.salary * 0.10
#         self.gross_salary= self.salary + hra + da
        
#         print("Name : ",self.name)
#         print("Gross Salary : ", self.gross_salary)
# e=Emp("Dani",34000)
# e.gross_salary()

#Q3:  Library Book System
# def new_func():
#     class Book:
#         def __init__(self,name,author,price):
#             self.name = name
#             self.author = author
#             self.price = price
#         def disp(self):
#             print("Name : ", self.name)
#             print("Author : ",self.author)
#             print("Price : ", self.price)
#             if self.price > 1000:
#                 print("Expensive")
#             else:
#                 print("Not Expensive")
#     b = Book ("CPP","Stroustrup",200)
#     b.disp()

# new_func()


#Q4: CALCULATE ELECTRICITY BILL ************
# class E_bill:
#     def __init__(self,C_name,unit_con):
#         self.C_name = C_name
#         self.unit_con = unit_con
#     def cal_bill(self):
#         bill = self.unit_con * 15
#         if bill > 5000:
#             disc= bill * 0.05
#             bill = bill - disc
#         print("Customer Name : ",self.C_name)
#         print("Unit Consumed : ",self.unit_con)
#         print("Final Bill : ",bill)
# e= E_bill("Dani",50)
# e.cal_bill()

#Q5: shopping Cart 🛒
# class shop:
#     def __init__(self,name,item,price):
#         self.name = name
#         self.item = item
#         self.price = price
#     def tot_bill(self):
#         bill = self.item * self.price
#         if bill> 1000:
#             disc = bill * 0.10
#             fin_bill = bill - disc
#         else:
#             fin_bill=bill



#         print("Name : ",self.name)
#         print("Bill : ", bill)
#         print("Final Bill :", fin_bill)
# s=shop("dani",5,2300)
# s.tot_bill()