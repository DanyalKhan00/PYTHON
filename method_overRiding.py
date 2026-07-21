# ******* ALL ABOUT METHOD OVER RIDING  ***********
# (1):
# class Emp:
#     def cal_sal(self):
#         print("Basic Salary : ")
# class manager(Emp):
#     def __init__(self,bas_sal, bonus):
#         self.bas_sal = bas_sal
#         self.bonus = bonus

#     def cal_sal(self):
#         print("Manager Salary : ",self.bas_sal + self.bonus)

# class Devolper(Emp):
#     def __init__(self,bas_sal, over_time):
#         self.bas_sal = bas_sal
#         self.over_time = over_time

#     def cal_sal(self):
#         print("Manager Salary : ",self.bas_sal + self.over_time)

# m = manager(45000,5600)
# m.cal_sal()
# d=Devolper(55000,7800)
# d.cal_sal()


#(2):
# class payment:
#     def pay(self):
#         print("payment process :")

# class creditcard(payment):
#     def pay(self):
#        print("payment made using creditcard")

# class jazzcash(payment):
#     def pay(self):
#         print("Payment Made using jazzcash")

# class easypaisa(payment):
#     def pay(self):
#         print("Payment Made using easypaisa")

# payment = [creditcard(),jazzcash(),easypaisa()]

# for i in payment:
#     i.pay()


#(3)
# class shape:
#     def area(self):
#         print("Area Cannot be calculated : ")
    
# class rectangle(shape):
#     def __init__(self, lenght , width):
#         self.length = lenght
#         self.width = width

#     def area(self):
#         print("Rectangle Area : ",self.length * self.width)

# class circle(shape):
#     def __init__(self,radius):
#         self.radius  = radius

#     def area(self):
#         print("Circle Area : ",3.14 * self.radius * self.radius)

# r = rectangle(5,6)
# r.area()

# c= circle(4)
# c.area()