# ******** ALL ABOUT METHOD OVERLOADING *********

#Q1
# class A:
#     def show(self):
#         print("WelCome ! ")

#     def show(self,firstname=''):
#         print("WelCome ! ,firstname")

#     def show(self,firstname='',lastname=''):
#         print("WelCome ! ",firstname,lastname)

# obj = A()
# obj.show()
# obj.show("Aimi")
# obj.show("Aimi","Dani")


#Q2:
# class Emp:
#     def cal_sal(Self):
#         print("Basic Salary Calculation")
# class manager(Emp):
#     def __init__(self,bas_sal,bonus):
#         self.bas_sal = bas_sal
#         self.bonus = bonus
#     def cal_sal(self):
#         total = self.bas_sal + self.bonus
#         print("Manager Salary",total)

# class Devolper(Emp):
#     def __init__(self,bas_sal,over_time):
#         self.bas_sal = bas_sal
#         self.over_time = over_time
#     def cal_sal(self):
#         total = self.bas_sal + self.over_time
#         print("Devolper Salary : ",total)

# m=manager(50000,4500)
# m.cal_sal()

# d= Devolper(70000,9800)
# d.cal_sal()


#Q3:
# class food:
#     def prepare(self):
#         print("Food is Preparing ....... ")
# class pizza(food):
#     def __init__(self,customer):
#         self.customer = customer
#     def prepare(self):
#             print(f"preparing pizza for : {self.customer}")


# class burger(food):
#     def __init__(self,customer):
#         self.customer = customer
#     def prepare(self):
#             print(f"preparing Burger for : {self.customer}")

# p = pizza("aimi")
# b = burger("Dani")
# b.prepare()
# p.prepare()
        