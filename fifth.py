#THIS INCLUDE THE PROGRAM TYPE QUESTION FROM THE FOLLOWING TOPIC.
"""1. SELECTION STATMENT
2. CONDTIONAL STATMENT
3. FUNCTION
4. RECURSION
5. STRING
7.LIST"""
#**************** SELECTION STATMENT *****************
#Question 1: Electricity Bill
#Write a program that calculates the electricity bill according to the following rules:
#Up to 100 units → Rs. 5 per unit
#101–200 units → Rs. 8 per unit
#Above 200 units → Rs. 10 per unit
"""units=int(input("Enter Electricity Unit"))
if units <=100:
    bill=units * 5
elif units <=200:
    bill=units * 8
else:
    bill=units * 10
print("Total Bill Are ",bill)"""
#Question 2: Character Checker
#Write a program that asks the user to enter a single character and prints whether it is:
#Uppercase letter
#Lowercase letter
#Digit
#Special character
"""ch=input("Enter Character")
if ch .isupper():
    print("Upper Case Letter")
elif ch .islower():
    print("Lower Case letter")
elif ch .isdigit():
    print("Digit ")
else:
    print("Special Character ")"""
#**************** CONDITIONAL STATMENT *****************
#Question 1: Sum of Even Numbers
#Write a program that asks the user for a number N and prints the sum of all even numbers from 1 to N.
"""n=int(input("Enter No:"))
sum=0
for i in range(2, n+1, 2):
    sum += i
print("Sum =" , sum)"""
#Question 2: Count Positive Numbers
#Write a program that asks the user to enter 7 numbers and counts how many are positive.
"""count=0
for i in range(7):
    num=int(input("Enter No: " ))
    if num>0:
        count+=1
print("Total Postive Integer Are : ", count)"""

