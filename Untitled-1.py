class student:
    def __init__(self,Name,marks,dept,clg):
        self.Name =  Name
        self.marks = marks
        self.dept = dept
        self.clg = clg
    def display(self):
        print("Name: ", self.Name)
        print("Mark: ", self.marks)
        print("dept: ", self.dept)
        print("clg: ", self.clg)

studentS = []
for i in range(5):
    print("--- Enter Detial ---",i+1)
    Name = input("Enter Name : ")
    marks = int(input("Enter Marks : "))
    dept = input("Enter Dept Name : ")
    clg= input("Enter CLg Name : ")
s= student(Name,marks,dept,clg)
students.append(s)
s.display()