#******************** LIST  ****************************

#**************LIST SLICING****************
#Ex1:Write a Python program that takes a list and prints every alternate element in reverse order
"""list=[12,34,56,89,43,56,78]
print(list[::-2])"""
#Ex2: Write a program to divide a list into two equal halves using slicing.
"""list=[2, 4, 6, 8, 10, 12]
mid=len(list)//2
first=list [:mid]
second=list[mid:]
print("First Part",first)
print("Last Part",second)
"""
#Ex3:Write a program that removes the first two and last two elements using slicing.
"""numbers = [5,10,15,20,25,30,35,40]
result=numbers[2:-2]
print(result)"""
"""list=["dani",12.4,89,"True"]
print(list[3])
list[3]="False"
print (list)
del (list[2])
print(list)"""
#Accessing Element /Traversing Element
"""numbers = [5,10,15,20,25,30,35,40]
for i in range(len(numbers)):
    print(numbers[i])"""
# ********************* LIST FUNCTION IN PYTHON ********************************
"""a=["dani",80,"zarar",90]
print(len(a))"""
#Ex2:Write a Python program that asks the user to enter 5 words. Using the len() function, count how many words have an even length and how many have an odd length.
"""odd=0
even=0
for i in range(5):
    word=input("Enter Word")
    if len(word) % 2==0:
        even+=1
    else:
        odd+=1
print("Total Even ",even)
print("Total Odd",odd)"""
"""#Ex3:Write a Python program that asks the user to enter 6 words. Print only those words whose length is greater than 4.
for i in range(6):
    word = input("Enter Word")
if len(word) > 4:
    print(word)"""
# ********************* MAX & MIN FUNCTION IN PYTHON ********************************
#Ex1:numbers = []
"""for i in range(5):
    item=int(input("Enter number"))
    numbers.append(item)
    print("Maximum Value is ",max(numbers))"""
#Ex2:Write a Python program that asks the user to enter 6 numbers into a list. Find the largest and smallest numbers and print their sum.
"""numbers=[]
for i in range(6):
    num=int(input("Enter Number"))
    numbers.append(num)
largest = max(numbers)
smallest = min(numbers)
print("Largest Number",largest)
print("Smallest Number",smallest)
print("Sum Of largest and Smallest",largest + smallest)"""
#Ex3:Write a Python program that asks the user to enter 5 numbers into a list. Find the largest number and display its index (position).
"""numbers=[]
for i in range(6):
    item=int(input("Enter Numbers"))
    numbers.append(item)
largest=max(numbers)
position=numbers.index(largest)
print("Largest No:",largest)
print("Index is",position)"""
#Ex4:Write a Python program that asks the user to enter 8 numbers into a list and prints the third smallest number using the min() function.
"""numbers=[]
for i in range(7):
    num=int(input("Enter No"))
    numbers.append(num)
first=min(numbers)
numbers.remove(first)
second=min(numbers)
numbers.remove(second)
third=min(numbers)
print("The Third Smallest Number is:",third)"""
#******************** APPEND FUNCTION ************************
#Ex1:
"""a=[]
for i in range(5):
    num=int(input("Enter No"))
    a.append(num)
print(a)"""
#Ex2:Write a Python program that asks the user to enter 10 numbers. Store only the even numbers in a new list using the append() function and display the new list.
"""even_num =[]
for i in range(5):
    num=int(input("Enter No"))
    if num% 2 == 0:
        even_num.append(num)
print("Even Number",even_num)
"""
#Ex3:Write a Python program that asks the user to enter 8 numbers. Store the positive numbers in one list and the negative numbers in another list using the append() function
"""positive = []
negative = []
for i in range(8):
    num=int(input("Enter No"))
    if num>0:
        positive.append(num)
    else:
        negative.append(num)
print("Total positive Number",positive)
print("Total Negative Number",negative)"""
#Ex4:Write a Python program that asks the user to enter 8 numbers. Store only the numbers that are divisible by 5 in a new list using the append() function and display the new list.
"""number = []
for i in range(8):
    num=int(input("Enter No"))
    if num % 5 ==0:
        number.append(num)
print("the Number Divisble by 5 is :",number)"""