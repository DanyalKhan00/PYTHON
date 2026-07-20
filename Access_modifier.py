# **** ALL ABOUT ACCESS MODIFER
# ==> PRIVATE
# ==> PROTECTED
# ==> PUBLIC

# Q1:Student Record (Public, Protected, Private)
# class student:
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self._roll= roll
#         self.__marks= marks
#     def disp(self):
#         print("Name: ",self.name)
#         print("Roll No :" , self._roll)
#         print("Marks : ", self.__marks)
# s= student("Aimi",21,88)
# s.disp()
# print("****************************")
# print("Name: ",s.name)
# print("Roll No :" , s._roll)
# print("Marks : ", s.__marks)    # this will give error because it is the private member

# Question 2: Bank Account (Private Variable)

# class bank:
#     def __init__(self,name,bln):
#         self.name = name
#         self.__bln = bln
#     def depo (self,amount):
#         self.__bln += amount
#         print("Amount Deposited Successfully ")

#     def show_bln (self):
#       print("Account Holder Name : ", self.name)
#       print("Current Balance : ",self.__bln)

# b= bank("Aimi",50000)
# b.depo(5000)
# b.show_bln()


# Q3:Employee Salary (Private Access Modifier)

# class Emp:
#     def __init__(self,name,dept,salary):
#         self.name = name
#         self._dept = dept
#         self.__salary = salary
#     def increase_sal(self,amount):
#         self.__salary += amount
#         print("Salary Updated SuccessFully")

#     def disp(self):
#         print("Emp Name : ",self.name)
#         print("Emp Name : ",self._dept)
#         print("Emp Name : ",self.__salary)
# e=Emp("Aimi","C-S",5000)
# e.disp()
# e.increase_sal(2000)

#Q4:  ATM Machine System

# class ATM:
#     def __init__(self,Acc_hol,Acc_no,bln):
#        self.Acc_hol = Acc_hol
#        self._Acc_no = Acc_no
#        self.__bln = bln
#     def deposit(self,amount):
#         self.__bln += amount
#         print("Deposit Successfully !")
#     def withdraw(self,amount):
#         if amount <=self.__bln:
#             self.__bln -= amount
#             print("With draw Successfully !")
#         else:
#             print("Insufficient Balance !")
#     def chk_bln(self):
#         print("Current balance :", self.__bln)
#     def display_info(self):
#         print("Account Holder:", self.Acc_hol)
#         print("Account Number:", self._Acc_no)

#     def display(self):
#         print("=== Account Details ===")
#         print("Account Holder:", self.Acc_hol)
#         print("Account Number:", self._Acc_no)
#         print("Current Balance:", self.__bln)  # Added balance here
#         print("=======================")

# atm=ATM("Aimi",27372163,75000)
# atm.deposit(9000)
# atm.withdraw(5000)
# atm.withdraw(6000)
# atm.chk_bln()
# atm.display()

  
 