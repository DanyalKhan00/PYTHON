# class student:
#     def __init__(self,Name,marks,dept,clg):
#         self.Name =  Name
#         self.marks = marks
#         self.dept = dept
#         self.clg = clg
        
#     def display(self):
#         print("Name: ", self.Name)
#         print("Mark: ", self.marks)
#         print("dept: ", self.dept)
#         print("clg: ", self.clg)
#         print("----------------------\n")
# students = []
# f = open("C:\\Users\\Officer Danyal\\Desktop\\python\\Downloads.txt", "w")
# for i in range(2):
#     print("--- Enter Detail ---",i+1)
#     Name = input("Enter Name : ")
#     marks = int(input("Enter Marks : "))
#     dept = input("Enter Dept Name : ")
#     clg= input("Enter CLg Name : ")
#     s= student(Name,marks,dept,clg)
#     students.append(s)
#    # print("----------------------\n")
#     f.write("Name :"+ Name + "\n")
#     f.write("Marks :"+ str(marks)+ "\n")
#     f.write("Dept :"+ dept + "\n")
#     f.write("Clg :"+ clg + "\n")
#     f.write("----------------------\n" )
# f.close()
# for s in students:
#     s.display()







# def calculate_salary(amount):
#     if amount > 1000:
#         bonus = amount * 0.10
#     else:
#         bonus = amount * 0.05
#     total_salary = amount + bonus
#     print("Salary:", amount)
#     print("Bonus:", bonus)
#     print("Total Salary:", total_salary)
# for i in range(3):
#     print("Enter salary of Employee", i + 1)
#     amount = float(input())
#     calculate_salary(amount)
#     print("----------------------")
