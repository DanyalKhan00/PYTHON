#   *** ALL ABOUT INHERITANCE   ***


# (1):    Single Inheritance .......

# class A:
#     num1=int(input("Enter First Number : "))
#     num2=int(input("Enter Second Number : "))
#     def Add(self):
#         print("Addtion is  :", self.num1 + self.num2)
#     def sub(self):
#         print("Subtraction  is  :", self.num1 - self.num2)
# class B(A):
#     def mul(self):
#         print("Multiplication is  :", self.num1 * self.num2)
#     def div(self):
#         print("Division  is  :", self.num1 /  self.num2)
#     def rem(self):
#         print("Reminder is:",self.num1 % self.num2)
# obj = B()
# obj.Add()
# obj.sub()
# obj.mul()
# obj.div()
# obj.rem()

#(2): Employee and Manager

# class Emp:
#     def __init__(self, name,salary):
#         self.name=name
#         self.salary= salary
#     def disp_emp(self):
#         print("Name : ",self.name)
#         print("Salary : " , self.salary)
# class manager(Emp):
#     def __init__(self,name,salary,dept):
#         super().__init__(name, salary)
#         self.dept = dept
#     def disp_man(self):
#          self.disp_emp()
#          print("Dept : ", self.dept)

# m=manager("Aimi",78000,"C-S")
# m.disp_man()

# (3) : Vehicle and Car


# class vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self . model = model
#     def disp(self):
#         print("Brand  : ", self.brand)
#         print("Model : ", self.model)
# class car(vehicle):
#     def __init__(self,brand,model, price):
#         super().__init__(brand,model)
#         self.price = price
#     def disp_car(self):
#         print("Price : ", self.price)
# c=car("Rolls-Royce","Ghost sedan",300000)
# c.disp()
# c.disp_car()

# (4): Person and Student

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def disp_per(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)
# class student(person):
#     def __init__(self,name,age,marks):
#        super().__init__(name, age)
#        self.marks = marks
#     def disp_res(self):
#         self.disp_per()
#         print("Marks : ",self.marks)
#         if self.marks >= 50:
#             print("Pass")
#         else:
#             print("Fail")
# s=student("Aimi",18,88)
# s.disp_res()
# print("********************")
# s1=student("Emo",18,38)
# s1.disp_res()


# (5) : Product and Electronics
# class product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def disp_pro(self):
#         print("Name : ",self.name)
#         print("Price : ", self.price)
# class electronic(product):
#     def __init__(self, name, price, warranty):
#         super().__init__(name, price)
#         self.warranty = warranty
#     def fin_pr(self):
#         self.disp_pro()
#         if self.price >= 50000:
#             discount = self.price * 0.10
#         else:
#             discount = 0
#         final_price = self.price - discount
#         print("Warranty : ",self.warranty, "year")
#         print("Discount : ",discount)
#         print("Final Price : ",final_price)
# e=electronic("Laptop",55000,3)
# e.fin_pr()

                

