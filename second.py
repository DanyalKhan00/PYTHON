#Ex1:Write a function lucky_number(num) that returns "Lucky" if the sum of the digits is divisible by 7; otherwise return "Not Lucky"
"""def lucky_number(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    if total % 7 == 0:
        return "Lucky"
    else:
        return "Not Lucky"
number = int(input("Enter Number: "))
print(lucky_number(number))"""
#Ex2:Print numbers from 1 to 40, but skip every number that is divisible by 4.
"""for i in range(1,41):
    if i%4==0:
        continue
    print(i)"""
#Ex3:Keep asking the user for numbers. Stop the program when a negative number is entered and print the total sum of all positive numbers.
"""sum=0
while True:
    n=int(input("Enter Number"))

    if n <0:
        break
    sum+=n
print("Total sum", sum)"""
#Ex4:Create a function grade(marks) that returns:
#A → 90 and above
#B → 80–89
#C → 70–79
#D → 60–69
#Fail → below 60
"""def grade(marks):
    if marks>=90:
        return "A"
    elif marks >=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks >=60:
        return "D"
    else:
        return "Fail"
n=int(input("Enter Marks"))
print(grade(n))"""
#Ex5:Print a hollow square of size 5 × 5.
"""row=5
for i in range(row):
    for j in range(row):
        if i==0 or i == row -1 or j == 0 or j == row -1:
             
             print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
        """
#Ex6:Create a function bonus(salary, years).
#More than 10 years → 20%
#5–10 years → 10%
#Less than 5 years → 5%
#Return the bonus amount
"""def bonus(salary, year):
    if year>=10:
        return salary * 0.20
    elif year <=5:
        return salary * 0.10
    else:
        return salary * 0.05
salary=float(input("Enter Your salary"))
year=int(input("Enter Your Experience Year"))
print("Bonus =", bonus(salary,year))"""
#Ex7:Ask the user to enter a password repeatedly.
#If password length is less than 6, print "Too Short" and continue.
#If password is "admin123", print "Login Successful" and stop.
#Otherwise print "Wrong Password".
"""while True:
    password=input("Enter Passowrd")
    if len(password)<6:
        print("Too Short")
        continue
    if password == "admin123":
        print("Login Successfull")
        break
    
    print("Wrong Password!")"""
#Ex8:Find the first number between 100 and 300 that is divisible by both 9 and 11, then stop searching.
"""for i in range(100, 301):

    if i % 9 == 0 and i % 11 == 0:
        print("Number =", i)
        break"""

#EX9:Write a Python program to calculate the electricity bill using the following rules:

#The first 100 units cost Rs. 5 per unit.
#The next 100 units cost Rs. 8 per unit.
#Any units above 200 cost Rs. 10 per unit.
#Print the total bill.
"""unit=int(input("Enter Electricity Unit"))
if unit<=100:
    bill=unit*5
elif unit<=200:
    bill= (100 * 5) +((unit-100)*8)
else:
    bill=(100 * 5)+ (100 * 8)+((unit - 200)*10)
print("Total bill",bill)
"""
#Ex10:Write a program that inputs a three-digit number and prints:
#Sum of digits
#Product of digits
#Whether the sum is greater than the product
"""num=int(input("Enter No:"))
a=num//10
b=(num//10) % 10
c=num%10
sum=a+b+c
print("Sum Of Digit is:", sum)
pro=a*b*c
print("Product of digit is :", pro)
print("Sum > product", sum>pro)
"""
#Ex11:A customer gets:
#25% discount if purchase is above 10000.
#15% discount if purchase is between 5000 and 10000.
#No discount otherwise.
#Display the final bill.
"""amount=float(input("Enter Your Purchase Amount"))
print("Your Purchase Amount is ", amount)
if amount >=10000:
    discount= amount * 0.25
elif amount >=5000:
    discount=amount * 0.15
else:
    discount=0
print("Discount", discount)
print("Final Bill", amount - discount)"""
#Ex12:Input the runs scored by a batsman.
#100 or more → Century
#50–99 → Half Century
#30–49 → Good Innings
#Otherwise → Needs Improvement
"""run=int(input("Enter Runs"))
print("Your Runs are", run)
if run>=100:
    print("Century")
elif run >=50:
    print("Half Century")
elif run >=30:
    print("Good Inning")
else:
    print("Need Improvement")"""
#Ex13:A person can apply for a passport only if:
#Age is 18 or above.
#Has a valid CNIC.
#Display whether the person is eligible.
"""age=int(input("Enter Age"))
cnic=input("You have cnic (yes/no)")
if age >=18 and cnic=="yes":
    print("Eligible For PassPort")
else:
    print("Not Eligibel")"""
#Ex14:A student gets a scholarship if:
#CGPA is at least 3.5 OR
#Sports certificate is available.
"""cgpa=float(input("Enter cgpa"))
sport_certificate=input("Do You Have Sports Certificate( yes/ no)")
if cgpa >=3.5 and sport_certificate =="yes":
    print("Eligible For Scholarship")
else:
    print("Not Eligible For Scholarship")
"""
#Ex15:Print the patter...
#1
#12
#123
#1234
#12345
"""for i in range(1,6):
    for j in range( 1, i+1):
        print(j,end="")
    print()"""
#Ex16: Print the pattern
"""*****
****
***
**
*
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()
"""
#Ex17:Keep taking numbers from the user until the user enters 999. Print the sum of all numbers except 999
"""total=0
while True:
    num=int(input("Enter number"))
    if num==999:
         break

    total+=num
print("sum of number are:", total)
"""
#Ex18:Print numbers from 1 to 20:

#Skip multiples of 4 using continue.
#Do nothing when the number is 15 using pass.
"""for i in range(1,21):

    if i % 4 == 0:
        continue

    if i==15:
        pass

    print(i)"""
#Ex19:Write a function count_vowels(text) that returns the number of vowels in a string
"""def count_vowel(text):
    count=0
    for ch in text:
        if ch in "aeiouAEIOU":
            count+=1
    return count
name=input("Enter String")
print("No of Vowel are",count_vowel(name))"""
#Ex20:Create a function login().
#The user has only 3 attempts to enter the correct password (python123).
#Use a loop.
#Use break when login succeeds.
#Use continue if the password is empty.
#Print "Account Locked" after 3 failed attempts
"""def login():
    attempt=0

    while attempt<3:
        password=input("Enter Password")
        if password=="":
            continue
        if password=="python123":
            print("Login Successfully")
            break
        attempt+=1
    else:
        print("Account Locked")

login()"""
#Ex21:Create a function student_result().
#The function should:
#Input marks of 5 subjects.
#Calculate the total and average.
#If the average is below 40, print Fail.
#Otherwise print Pass.
#Finally, print the following pattern based on the average:
#If Pass → print *****
#If Fail → print ***
"""def student_result():
    total=0
    for i in range(5):
        marks=int(input("Enter 5 Subject Marks"))
        total+=marks
    print("Your Total marks is ",total)
    avg=total/5
    print("Your Average Marks is:",avg)
    if avg >=40:
        print("Pass")
        for i in range(5):
            print("*",end="")
    else:
        print("Fail")
        for i in range(3):
            print("*",end="")
student_result()"""
print("This is me danyal khan")