# print function
"""a=10
b=90
c=a+b
print("the value of a is",a,"the value of b is",b,"And the Addition of a & b is",c)"""

# INPUT FUNCTION
# Ex1:
"""Name=input("Enter  Your Name")
print("Welcome Mrs.",Name)"""
#Ex2:
"""num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))
sum=num1+num2
print("The Sum is ",sum)"""
#Ex3:
# Write a python program that takes a student name, age and city as input and print the information in a readable format.....
"""name=input("Enter Your Name:)")
age=int(input("Enter Your age:)"))
city=input("Enter Your City Name:)")
print("\n*******Student Info*************")
print("Name:",name)
print("Age:",age)
print("City:",city)"""

#Ex4:
#Take marks of three Subject from the user . calculate and displayed their Total and Average Marks.....
"""sub1=float(input("Enter the 1st Subject Marks"))
sub2=float(input("Enter the 2nd Subject Marks"))
sub3=float(input("Enter the 3rd Subject Marks"))
total=sub1+sub2+sub3
print("The Total Marks is:",total)
Avg=total/3
print("The Average Marks is:",Avg)"""
#Ex5:
#input an employee Monthly salary and calculate the annual salary......
""""mon_sal=float(input("Enter Monthly Salary"))
print("Your Monthly Salary is :",mon_sal)
annual_sal=mon_sal*12
print("Your Annual salary is :",annual_sal)"""
#Ex6:
# A customer Buy 3 Products. Input Prices of all three product and calculate the total Bill.........
"""p1=int(input("Enter the Product 1 price:"))
p2=int(input("Enter the Product 2 price:"))
p3=int(input("Enter the Product 3 price:"))
total_bill=p1+p2+p3
print("The Total Bill of 3 product are: ", total_bill)"""
#Ex7:
#input the number of minutes and Convert it into hours and remaining minutes.....
"""min=int(input("Enter the Minutes"))
hours=min//60
print("The total Hours are:",hours)
rem=min%60
print("The Remaining Minutes are", rem)"""
#Ex8:Take principal ,Rate,and time as input and Calculate the Simple Interst..
#: Simple interst Formual : SI=(P x R x T)/100
"""principal=float(input("Enter Principal:"))
Rate=float(input("Enter Rate:"))
time=float(input("Enter Time:"))
si=(principal*Rate*time)//100
print("The Total simple Interst are: ",si)"""
#Ex8: Input the Number of electricity unit Consumed. if each unit costs 25 rupees, calculate the total bill ........
"""units=int(input("Enter Units Consumed:"))
bill= units*25
print("The Total units are",units,"and the total Bills are", bill)"""
#Ex9: Input the original price of an item and the discount percentage. calculate the discount amount and final price...
"""org_pr=float(input("Enter the Original Price:"))
discount=float(input("Enter Discount % "))
discount=(org_pr*discount)/100
final_price=org_pr-discount
print("The Orignal price is:",org_pr,"And the Discount price is",final_price)"""
# OPERATOR
 # (1) ARITHAMATIC OPERATOR.......
#Ex1: Write a program that takes the marks of 5 subject as input calcualte total marks, avg marks and percentage...
"""sub1=float(input("Enter 1st Subject Marks"))
sub2=float(input("Enter 2nd Subject Marks"))
sub3=float(input("Enter 3rd Subject Marks"))
sub4=float(input("Enter 4th Subject Marks"))
sub5=float(input("Enter 5th Subject Marks"))
total_marks=sub1+sub2+sub3+sub4+sub5
print("The Total Marks are: " , total_marks)
avg=total_marks/5
print("The average Marks of 5 subject are: " , avg)
percentage=(total_marks/500)*100
print("Your Percentage is : " , percentage)"""
#Ex2:write a python program that takes the prices of 3 product as input. calculate total price, 10% disc, and final price.
"""p1=float(input("Enter The 1st product Price:"))
p2=float(input("Enter The 2nd product Price:"))
p3=float(input("Enter The 3rd product Price:"))
total_price= p1+p2+p3
print("The Total price of 3 product are " , total_price)
discount=total_price *10/100
print("The total discount on product are: ", discount)
final_price=total_price - discount
print("The Final Price of All products are:", final_price)"""
#Ex3: Write a python program that take the basic salary as input , HRA=20% and DA=15% calculate and display the gross salary..
"""bas_sal=float(input("Enter Your Basic Salary"))
hra=bas_sal*20/100
print("HRA=",hra)
da=bas_sal*15/100
print("DA=",da)
gross_sal=bas_sal+hra+da
print("The Gross Salary are", gross_sal)"""
#Ex4: Write a program that take the principal, rate, and time as input. calculate the simple interst and Total Amount.....
"""principal=float(input("Enter the Principal: "))
rate=float(input("Enter the Rate: "))
time=int(input("Enter the time : "))
simple_interst=(principal*rate*time)/100
print("The simple interst are:", simple_interst)
total_amount=principal+simple_interst
print("The total amount are :", total_amount)"""
#(2): RELATIONAL / COMPARISON OPERATOR...
#Ex1:write a program that take two number is input and display which number is larger. if both number are equal, display a suitable message.
"""num1=int(input("Enter 1st Number"))
num2=int(input("Enter 2nd Number"))
if num1>num2:
    print("1st Number is Larger")
elif num1<num2:
    print("2nd Number is larger")
else:
    print("Both are Equal")"""
#Ex2: Write a program that take integer as an input and chk whether it is odd or even
"""num=float(input("Enter Number"))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")"""
#Ex3:Write a program that take a person age as input and chk whether they are eligible to vote. a person is eligible if their age is 18 or above
"""age=int(input("Enter Your Age:"))
if age>=18:
    print("Eligable For Vote:")
else:
    print("Not Eligable for vote:")"""
#(3): ASSIGNMENT OPERATOR......
#Ex1:write a program that takes an emp salary as input increase the salary by 5000 using += diplsy updated salary.....
"""salary=float(input("Enter Salary:"))
print("YOur salaey is", salary)
up_salary=salary+5000
print("Your salary is",salary,"and your updated salary is :",up_salary)"""
#Ex2:
#write a prgram that take the inital bank balance as input takes the amount to withdrae update the bln using-=..
"""bln=float(input("Enter salary"))
withdraw=float(input("Enter the Withdraw amount"))
bln=bln -withdraw
print("Remaining bln", bln)"""
#(4): LOGICAL OPERATOR........
#Ex1: write a program that takes a student maths and eng marks as input a student is eligable for addmission only if: maths marks >=50 & eng marks>=50. otheriwise print Not eligible
"""math=int(input("Enter maths marks"))
print("marks of maths are:", math)
Eng=int(input("Enter English marks"))
print("marks of Eng are:", Eng)
if math >=50 and Eng>=50:
    print("Eligible For Addmission:")
else:
    print("Not Eligible")"""
#Ex2: write a prgram that ask the user for a username, and password the correct username is dani and the correct password is 147248. if both are correct , print"Login Successfull", otherwise print"invalid UserName or Password".
"""username=input("Enter Your UserName")
password=input("Enter Your Password")
if (username=="dani"and password=="147248"):
  print("Login Successful")
else:
  print("Invalid UserName or Password")"""
#Ex3: write a python program that takes a student percentage and family income as input if percentage is 90 or above, or family income is less than 30,000 otherwise print "Not Eligible"
"""percentage=float(input("Enter Your Percentage"))
income=float(input("Enter Your Income"))
if(percentage>=90 and income<=30000):
    print("Eligible For Scholarship")
else:
    print("Not Eligiblee")"""
#Ex4: write a program that ask the user whether they are banned . if the user enter yes, print"Access Denied". otherwise, print"Access Granted"
"""banned=input("Are You Banned(yes/no)")
if not(banned=="yes"):
    print("Access Granted")
else:
    print("Access Denied")"""
#(4): IDENTITY OPERATOR........
#Ex1: write a program that assign one variable to another and uses the is operator to chk whether both variables refer to the same object...
"""num1=100
num2=num1
if num1 is num2:
    print("Both variables refer to the same object")
else:
    print("Both variables refer to the differnet object")"""
#Ex2: create two separte list with the same values and uses the is not operator to chk whether they are different object....
"""list1=[10,20,30]
list2=[10,20,30]
if list1 is not list:
    print("Both lists are different object")
else:
    print("Both lists are same object")"""
#(5): MEMBERSHIP OPERATOR........
#Ex1:store some courses in a list ask the student to enter the course they want to enroll in if the course is available display availble otherwise not available......
"""courses=["python","java", "c","C++","javascript","PHP"]
course=input("Enter The course:")
if course in courses:
    print("Congradulation! You have been enrolled in the course")
else:
    print("This course is not available")"""
#Ex2: write a program that ask the user to enter a username if the username is already register, display login successful otherwise username not found plx register first........
"""usernames=["Aiman","Danyal","Sana","Marwa","Sundus","Madiha","Samreen"]
username=input("Enter Your UserName:")
if username in usernames:
    print("Login Successfull")
else:
    print("UserName not found please Register First:")"""
# MIX QUESTION ........
#Ex1: write a program to accept electricity unit consumption and calculate total price at the rate of 5 R.s unit. give a discount of 10% on all over bill
"""unit=int(input("Enter Electricity Unit Consumed :" ))
bill=unit * 5
print("Electricity bill", bill)
discount= bill*0.10
print("The total discount is", discount)
total_bill=bill - discount
print("Total bill to pay:", total_bill)"""
#Ex2:Write a program to accept marks of 5 subject and find the total marks and percentage assuming full marks as 100 in each subject..
"""sub1=float(input("Enter Sub1 Marks:"))
sub2=float(input("Enter Sub2 Marks:"))
sub3=float(input("Enter Sub3 Marks:"))
sub4=float(input("Enter Sub4 Marks:"))
sub5=float(input("Enter Sub5 Marks:"))
total= sub1+sub2+sub3+sub4+sub5
print("Total Marks is ", total)
percentage=(total/500)*100
print("Percentage is ", percentage,"%")"""
#Ex3:Write a program to swap to values
"""v1=int(input("Enter 1st value:"))
v2=int(input("Enter 2nd value:"))
print("value Before swaping", v1,v2)
temp=v1
v1=v2
v2=temp
print("Value After Swaping", v1,v2)"""
"""#Ex4: write a program to accept total sales and find the profit amount at the @ 5%
total_sales=float(input("Enter total sales amount:"))
print("Total sales amount are",total_sales)
profit=total_sales * 0.05
print("Total sales at the profit of 5% is :",profit)"""
#Ex5: write a program to accept two number chk whether the 1st number is greater than the 2nd and the sum of both number is greater than 100. if both are true print"Condtion is True" otherwise print "Condtion is False"
"""n1=int(input("Enter the 1st Number:"))
n2=int(input("Enter the 2nd Number"))
if n1>n2 and (n1+n2>100):
    print("Condtion is true")
else:
    print("Condtion is not true")"""
#Ex6:
#write a program to accept the Emp basic salary increase the salary by 10% using an assignment operator(+=). if the updated salary is > 50000 print"High salary" else print("Low salary")
"""basic_salary=float(input("Enter Basic Salary"))
basic_salary+=basic_salary*0.10
print("The Updated Salary is ", basic_salary)
if basic_salary>50000:
    print("High Salary")
else:
    print("Low Salary")"""
# ********* CONTROL STATMENT ***************
#1: (IF STATMENT)
#Ex1: write a program to chk whether a person is eligible for vote or Not....... eligiblity criteria is ( >=18 Yrs)
"""age=int(input("Enter Your Age:"))
print("Your Age is:",age)
if age>=18:
    print("You Are Eligible For Vote")
else:
    print("You are Not Eligible")"""
#Ex2: Write a program to find max between two number....
"""n1=float(input("Enter 1st Number"))
print(" Your First Number is :",n1)
n2=float(input("Enter 2nd Number"))
print(" Your Second Number is :",n2)
if n1>n2:
    print("the max number is n1", n1)
else:
    print("The maximum Number is n2",n2 ")"""
#Ex3: Write a program to find maximum between three number
"""n1=float(input("Enter 1st Number"))
print(" Your First Number is :",n1)
n2=float(input("Enter 2nd Number"))
print(" Your Second Number is :",n2)
n3=float(input("Enter 3rd Number"))
print(" Your third Number is :",n3)
if n1>n2 and n1>n3:
    print("the max number is n1", n1)
elif n2>n1 and n2>n3:
    print("The maximum Number is n2",n2 )
else:
    print("The Maximum Number is ", n3)"""
#Ex4: write a program to chk whether a given number is positive , negative or zero.....
"""num=float(input("Enter a Number to Chk:"))
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")"""
#Ex4:write a program to find the middle number in a group of three......
"""a=int(input("Enter a number"))
b=int(input("Enter b number"))
c=int(input("Enter c number"))
if (a>b and c>a) or (a<b and a>c):
    print("middle Number is a ",a)
elif(b>a and b<c) or(b<a and b>c):
    print("middle number is b",b)
else:
    print("middle number is C",c)"""
#Ex5:Write a program to take 5 subject marks , calculate total ,and find percentage and give grade on the following criteria.
# marks>=80 A   marks>=60 B         marks>=40 C         marks<40 D
"""sub1=int(input("Enter sub1 marks:"))
sub2=int(input("Enter sub2 marks:"))
sub3=int(input("Enter sub3 marks:"))
sub4=int(input("Enter sub4 marks:"))
sub5=int(input("Enter sub5 marks:"))
total_marks= sub1+sub2+sub3+sub4+sub5
print("The total marks is ", total_marks)
percentage=(total_marks/500)*100
print("Your Percentage is :", percentage)
if percentage >=80:
    print("Grade A")
elif percentage >=60 and percentage <80:
    print("Grade B")
elif percentage >=40 and percentage <60:
    print("Grade C")
else:
    print("Grade D")"""
#Ex6:Write a Python program to check whether a given year is a leap year.
"""year=int(input("Enter Year"))
if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a leap year")"""
#Ex7:Calculate electricity bill according to:
#First 100 units → Rs.5/unit
#Next 100 units → Rs.8/unit
#Above 200 units → Rs.10/unit
"""units = int(input("Enter units: "))
p
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 8)
else:
    bill = (100 * 5) + (100 * 8) + ((units - 200) * 10)

print("Electricity Bill =", bill)"""
#Ex8:Write a program that performs addition, subtraction, multiplication, or division based on the user's choice.
"""a=float(input("Enter Number"))
b=float(input("Enter Number"))
choice=input("Enter Operator(+,-,*,/):")
if choice=="+":
    print("You Hit + so it will perform Addition ", a+b)
elif choice=="-":
    print("You Hit - so it will perform Subtraction ", a-b)
elif choice=="*":
     print("You Hit * so it will perform multiplication ", a*b) 
elif choice=="/":
     print("You Hit / so it will perform Division ", a/b)
else:
     print("Invalid Operator") """
#Ex9: A student is eligible for admission if:Marks ≥ 60 and Age ≤ 25 Display whether the student is eligible.
"""marks=float(input("Enter Your Marks:"))
age=int(input("Enter Your Age:"))
if marks >=60 and age <=25:
    print("Eligible For Addmission")
else:
    print("Not Eligble For Addmission")"""
#Ex10:Calculate discount: Purchase ≥ 5000 → 20% && Purchase ≥ 3000 → 10 && Otherwise → No Discount
"""purchase_amount=float(input("Enter Purchase Amount"))
if purchase_amount >=5000:
    discount= purchase_amount * 0.20
    print("Discount ", discount)
    print("total amount",purchase_amount - discount)
elif purchase_amount >=3000:
        discount=purchase_amount * 0.10
        print("Discount ", discount)
        print("total amount",purchase_amount - discount)
else:
     discount=0
     print("Discount ", discount)
     print("total amount",purchase_amount - discount)"""
#Ex11: Input three sides and determine whether the triangle is:
#Equilateral
#Isosceles
#Scalene
"""side1=float(input("Enter Side 1"))
side2=float(input("Enter Side 1"))
side3=float(input("Enter Side 1"))
if side1==side2 == side3:
    print("Equliterial Trianlge")
elif side1==side2 or side2==side3 or side3==side1:
    print("Isolsceles Triangle")
else:
    print(" Scalene Trianlge")"""
#Ex12:Suppose your account balance is Rs. 10,000. Input withdrawal amount.

#Conditions:
#Withdrawal amount must be less than or equal to balance.
#Withdrawal amount must be a multiple of 500.
#Display success or an error message.
"""balance=10000
withdraw=int(input("Enter Withdrawl Amount:"))
if withdraw <= balance and withdraw %500==0:
      print("Withdraw Successfull", withdraw)
      remaining_bln=balance-withdraw
      print("Remaining amount are ", remaining_bln)
else:
     print("insufficent balance")"""
# ******* MINI PROJECT: STUDENT SCHOLARSHIP ELIGIBLITY SYSTEM.
"""Ask the user to enter:
Student Name,Age ,Marks (out of 100),Family Income
A student is eligible for a scholarship if:
Marks are 80 or above, and Family income is less than or equal to Rs. 50,000, and Age is between 17 and 25 years (inclusive).
If the student is eligible: Display "Congratulations! You are eligible for the scholarship." 
If marks are 90 or above, also display "You will receive a Full Scholarship."
Otherwise, display "You will receive a Partial Scholarship."
If the student is not eligible, display "Sorry! You are not eligible for the scholarship"""

"""name=input("Enter Your Name:")
print("Name :", name)
age=int(input("Enter Your Age"))
print("Age :", age)
marks=float(input("Enter Your Marks:"))
print("Marks:", marks)
income=float(input("Enter your Family Income"))
print("Family Income:", income)
if marks >= 80 and income <= 50000 and age >= 17 and age <= 25:
      print("Congratulations! You are eligible for the scholarship")
      if marks >= 90:
        print("You will receive a Full Scholarship")
      else:
        print("You will recieve partial Scholarship")
else:
  print("/n Sorry !",name)
  print("You are not eligible for scholarship")  """
#       ************ 2ND MINI PROJECT *************************
"""name = input("Enter Name: ")
print("Name:", name)

purchase_amount = float(input("Enter Purchase Amount: "))
print("Purchase Amount:", purchase_amount)

member = input("Are You A Member (yes/no): ")

discount = 0

if member == "yes":
    if purchase_amount >= 5000:
        discount = purchase_amount * 0.20
    else:
        discount = purchase_amount * 0.10
else:
    if purchase_amount >= 5000:
        discount = purchase_amount * 0.10
    else:
        discount = 0

final_bill = purchase_amount - discount

if final_bill > 3000:
    delivery = 200
else:
    delivery = 0

payable = final_bill + delivery

print("\n------- BILL -------")
print("Customer Name :", name)
print("Original Bill :", purchase_amount)
print("Discount      :", discount)
print("Delivery      :", delivery)
print("Final Bill    :", payable)"""
#*************** LOOPING *******************
# ***********    WHILE LOOP ********************
#Ex1: Write a program to print from 1 to 10
#i=1
#while i <= 10:
    #print(i)
    #i=i+1
#Ex2: write a program to print from 1 to n
"""n=int(input("Enter the number you want to print"))
i=1
while i<=n:
    print(i)
    i=i+1"""
#Ex3: Write a program to print number from n to 1
"""n=int(input("Enter the number you want to print in reverse"))
#n=1
while n>=1:
    print(n)
    n=n-1"""
#Ex4: write a program to print the number from 1 to n and also find their sum
"""n=int(input("Enter number"))
sum=0
i=1
while (i<=n):
    sum=sum+i
    i=i+1
    
    print("sum",sum) """
#Ex4: write a program to print the number from 1 to n and also find their square
"""n=int(input("Enter number to find square"))
i=1
sum=0
while i<=n:
    sum=sum+(i*i)
    i=i+1
    print("square",sum)"""
#Ex5: write a program to print the number from 1 to n and also find their Cube..
"""n=int(input("Enter Number"))
i=1
sum=0
while(i<=n):
    sum=sum+(i*i*i)
    i=i+1
print("Cube",sum)"""

#Ex6: write a program to print even number form 1 to n
"""n=int(input("Enter Number"))
i=0
while(i<=n):
    i+=2
    print(i)"""
#Ex7: write a program to find the sum of even number from 1 to n
"""n=int(input("Enter Number"))
i=2
sum=0
while(i<=n):
    sum=sum+i
    i=i+2
    print("sum",sum)"""
#******** MIX PROGRAM ON LOOP ************************
#Ex1:Write a Python program to input a number N and calculate the sum of all even numbers from 1 to N using a for loop.
"""n=int(input("Enter Number:"))
sum=0
for i in range(2,n+1,2):

    sum=sum+i
    print("Sum is :", sum)"""
#Ex2:Write a Python program to count the number of digits in a given integer using a while loop.
"""num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Total digits =", count)"""
"""largest = float('-inf')
for i in range(5):
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
print("Largest number =", largest)"""
#Ex3:Write a Python program to calculate the sum of the digits of a number using a while loop.
"""num=int(input("Enter Number:"))

sum=0

while num>0:
    digit = num % 10
    sum += digit
    num //=10

    print("Sum of digit are",sum)"""
#Ex4:Write a Python program to print all factors of a given number using a for loop.
"""num=int(input("Enter Number:"))
print("Factor are")
for i in range(1,num+1):
    if num% i==0:
        print(i)"""
#Ex5:Write a Python program to find the largest digit in a given number using a while loop.
"""num=int(input("Enter Number:"))
largest=0
while num>0:
    digit=num%10"""
#********* FUNCTION *******************
"""def message():
      print("Hello")

message()
"""
"""x=int(input("Enter No"))
y=int(input("Enter No"))
def addition(x,y):
print("Addition =",x+y)
addition(x,y)
print("Addition =",x+y)
addition(x,y)"""
print("hello Danyal")
print("This is me danyal khan")
