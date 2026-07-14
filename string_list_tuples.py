# This files Contain All Program Based On String, List and Tupples...........
#Q1: Write a Python program to accept a string from the user and count the number of uppercase letters, lowercase letters, digits, and special characters.
"""string=input("Enter String : ")
upper=0
lower=0
digit=0
special=0
for ch in string:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
    elif ch.isdigit():
        digit = digit + 1
    else:
        special = special + 1
print("Upper Case Letter : ", upper)
print("Lower Case Letter : ", lower)
print("Digit : ", digit)
print("Special Character : ", special) """
#Q2:Write a Python program to accept a sentence from the user and print the longest word and its length.
"""string = input("Enter Sentence : ")
word = string.split()
longest = word[0]
for words in word:
    if len(words) > len(longest):
        longest = words
print("Longest Word " , longest)"""

# ***************** LIST *******************
#Q1:Write a Python program to separate even and odd numbers into two different lists.
"""list = []
size = int (input("Enter List Size : "))
for i in range(size):
    num = int (input("Enter Element Of List : "))
    list.append(num)
odd = []
even = []

for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Odd : ", odd)
print("Even : ",even)"""

#Q3: Write a Python program to remove duplicate elements from a list without changing the original order.
"""list = []
size = int(input("Enter List Size : "))
for i in range(size):
    num = int(input("Enter List Element : "))
    list.append(num)

new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print("Orignal List : ", list)
print("New List : ", new_list)"""

# *************** TUPPLES *********************
#Q1:Write a Python program to accept a tuple of integers and print the sum and average of its elements.
"""tup = ()
size = int (input("Enter Tupple Size : "))
for i in range(size):
    num = int(input("Enter Tupple Element : "))
    tup= tup + (num,)
total =  sum(tup)
avg = total / len(tup)
print("Total Sum :  ", total)
print("Average Is : ", avg)"""


#Q2: Write a Python program to accept a tuple of integers and print the sum and average of its elements.
"""tup1 = ()
size = int (input("Enter Tupple1 Size : "))
for i in range(size):
    num = int(input("Enter Tupple1 Element : "))
    tup1= tup1 + (num,)

tup2 = ()
size = int (input("Enter Tupple2 Size : "))
for i in range(size):
    num = int(input("Enter Tupple2 Element : "))
    tup2= tup2 + (num,)

for i in tup1:
    if i in tup2:
        print("Common Element are : ", i)"""

# Q3: Write a Python program to remove duplicate values from a tuple and create a new tuple.
"""tup = ()
size = int(input("Enter tuple size: "))
for i in range(size):
    num = int(input("Enter element: "))
    tup = tup + (num,)
new_tup = ()
for i in tup:
    if i not in new_tup:
        new_tup = new_tup + (i,)
print("Original Tuple =", tup)
print("New Tuple =", new_tup)"""