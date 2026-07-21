# CLASS AND OBJECT
#(1)   STUDENT GRADE MANAGMENT....
# class student:
#     def __init__(self, name,m1,m2,m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self .m3 = m3
#     def total(self):
#         return self.m1 + self.m2 + self.m3
#         #print("Total Marks : ",total)
#     def avg(self):
#         return self.total()/3
#         #print("The Avg Marks is :",avg)
    
#     def disp(self):
#         print("Name : ", self.name)
#         print("Total  : ",self.total())
#         print("Average : ",self.avg())
# s = student("Aimi",90,88,89)
# s.total()
# s.avg()
# s.disp()

#(2)        LIBRARY BOOK SYSTEM ....
# class book:
#     def __init__(self,book_tit,author,price):
#         self.book_tit = book_tit
#         self.author = author
#         self.price = price

#     def disc(self):
#         self.price -= self.price * 0.10

#     def disp(self):
#         print("Title : ", self.book_tit)
#         print("Author : ",self.author)
#         print("Price : ",self.price)

# b= book("Atomic Habit", "james Clear", 1000)
# b.disc()
# b.disp()


#  CONSTRUCTOR
#(1)   EMPLOYEE SALARY ....

# class Emp:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def cal_sal(self):
#        return self.salary + self.salary * 0.15

# e= Emp("Aimi",45000)
# print("Total Salary ",e.cal_sal())


#(2)  PRODUCT BILLING
# class product:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def tot_bill(self):
#         return self.price * self.quantity
    
# p=product("cream",250,15)
# print("Total Bill : ", p.tot_bill())


 #  CONSTRUCTOR
#(1)   BANK ACCOUNT ....

# class bank_Acc:
#     def __init__(self,name,bln,pin):
#         self.name=name
#         self._bln= bln
#         self.__pin= pin

#     def show(self):
#         print(self.name)
#         print(self._bln)
#         print(self.__pin)
# obj = bank_Acc("Aimi",90000,250121)
# print("Name : ",obj.name)
# print("Balance : ", obj._bln)
# obj.show()

#(2)    MOBILE PHONE ....

# class mobile:
#     def __init__(self,model,per,pin):
#         self.model = model
#         self._per = per
#         self.__pin = pin
    
#     def show(self):
#         print(self.model)
#         print(self._per)
#         print(self.__pin)
# m = mobile("Iphone",90,1221)
# print(m.model)
# print(m._per)
# m.show()

# INHERITANCE ....
#(1)    VEHICLE SYSTEM
# class vehicle:
#     def __init__(self):
#         print("This is a vehicle")
# class bike(vehicle):
#     def disp(self):
#         print("This is Bike Class")

# class car(vehicle):
#     def disp(self):
#         print("This is car Class")

# b = bike()
# b.disp()
# c = car()
# c.disp()


#(2) EMPLOYEE HIERARCHY ....


# class emp:
#     def __init__(self):
#         print("This is the Emp class :")

# class manager(emp):
#     def __init__(self,salary,bonus):
#         self.salary = salary
#         self.bonus = bonus
#     def man_sal(self):
#         print(self.salary + self.bonus)

# class devolper(emp):
#     def __init__(self,salary , overtime):
#         self.salary = salary
#         self.overtime = overtime
#     def dev_sal(self):
#         print(self.salary + self.overtime) 

# m= manager(50000,1200)
# m.man_sal()
# print("======================")
# d=devolper(70000,2000)
# d.dev_sal()

        

# ABSTRACT CLASS / METHOD ........
#(1):   PAYMENT GATEWAY....

# from abc import ABC, abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass

# class  jazzcash(payment):
#         def pay(self):
#          print("Paid Through jazzcash")
# class easypaisa(payment):
#      def pay(self):
#          print("Paid Through Easy Paisa :")
# j = jazzcash()
# e= easypaisa()
# j.pay()
# e.pay()

# # (2): SHAPE ....

# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class rect(shape):
#     def __init__(self,l,w):
#         self.l= l
#         self.w=w
#     def area(self):
#         print(self.l * self.w)

# class circle(shape):
#     def __init__(self,r):
#         self.r=r

#     def area(self):
#         print(3.14 * self.r * self.r)
# rect(3,4).area()
# circle(3).area()


# POLYMORPHISM ...........
#(1) NOTIFICATION SYSTEM ....
 
# class email:
#     def send(self):
#         print("Email Send")

# class sms:
#     def send(self):
#         print("SMS send")

# class pushNotification:
#     def send(self):
#         print("Push Notification Send ")
# notification = [email(), sms(), pushNotification()]
# for n in notification:
#     n.send()

#(2)  ANIMALS SOUND ......

# class Dog:
#     def sound(self):
#         print("Dog is barking")
# class Cat:
#     def sound(self):
#         print("Cat Is Meowing")
# class Cow:
#     def sound(self):
#         print("Cow Is Owing")
# animal=[Dog(), Cat(),Cow()]
# for a in animal:
#     a.sound()

# METHOD OVERLOADING ....
#(1) CALCULATOR ....

# class calculator:
#     def add(self,a,b,c=0):
#         return a + b + c
# obj= calculator()
# print(obj.add(4,5))
# print(obj.add(4,5,3))

#(2) Area Calculator ....


# class area:
#     def area(self, l,w=None):
#         if w is None:
#             print("Square : ", l * l)
#         else:
#             print("Rectangle:", l * w)
# a= area()
# a.area(4)
# a.area(3,8)


# METHOD OVERRIDING....
# (1)Food Ordering ....

# class food:
#     def prerpare(self):
#         print("Preparing Food ")
# class pizza(food):
#     def prerpare(self):
#         print("Pizza Is Preparing ")
# class Burger(food):
#     def prepare(self):
#         print("Burger Is Preparing ")

# pizza().prerpare()
# Burger().prepare()

#(2):   REPORT GENERATOR ....
# class report:
#     def generate():
#         print("Report is Genereating")

# class PDFReport(report):
#     def generate(self):
#         print("Generating Pdf Report")

# class ExcelReport(report):
#     def generate(report):
#         print("Excel Report Is generating")

# p=PDFReport()
# excel=ExcelReport()
# p.generate()
# excel.generate()

    
        