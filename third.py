# ******     CHAPTER:: STRING   ******
# STRING CONCETANATION OPERATOR
#Ex1:
"""first_name=input("Enter Your First Name")
last_name=input("Enter Your Last Name")
full_name=first_name + last_name
print("Your Full Name is:",full_name)"""
"""#Ex2:Write a program that takes a first name and last name and creates an email address in the format:firstname.lastname@gmail.com
first_name=input("Enter first Name")
last_name=input("Enter last Name")
email=first_name + last_name +"@email.com"
print(email)"""
#Ex3:Write a program that takes:
#Student Name
#Roll Number
#Print the result in the format:
#Ali-23-CS-101
"""student_name=input("Enter Student Name")
roll_no=input("Ente Your Roll No")
student_id=student_name + "-" + roll_no
print(student_id)
"""
#Ex4:Write a program that creates a username by joining:
#First 3 letters of the first name
#Last 3 letters of the last name
"""first=input("Enter Your First Name")
last=input("Enter Your Last Name ")
user_name=first[:3] + last [-3:]
print("Your User Name is : ",user_name)"""
#Ex5:Take three words from the user and print them as one sentence.
"""word1=input("Enter 1st word")
word2=input("Enter 2nd word")
word3=input("Enter 3rd word")
sentence= word1 + " " + word2 + " " + word3
print("sentence:)",sentence)"""



# STRING REPLICATION OPERATOR
#Ex1:"""first_name=input("Enter Your First Name")
"""last_name=input("Enter Your Last Name")
full_name=first_name + last_name
print("Your Full Name is:",3*full_name)"""
#Ex2:Write a program that takes a word and a number n. Print the word n times.
"""word=input("Enter a Word")
number=int(input("Enter a number"))
result=word * number
print(result)"""
#Ex3:Write a program that asks the user for a password and prints stars (*) equal to the password length.
"""password=input("Enter Password")
print("*" *len(password))"""
#Ex4: Write a program that takes a symbol and a number, then prints that symbol repeated that many times.

"""symbol=input("Enter A Symbol")
number=int(input("Enter a Number"))
print(symbol *  number)"""
#Ex5:Write a program that takes a message and prints a banner above and below it using =.
"""message=input("Enter a Message")
line="*" * (len(message)+4)
print(line)
print(message)
print(line)"""
#STRING SLICING OPERATION
#Ex3: Write a program that prints the first 4 characters of a string.
"""string=input("Enter A String")
print(string[0:5])"""
#Ex4: Write a program that prints the last 3 characters of a string
"""string=input("Enter A String")
print(string[-3:])"""
#Ex5:Write a program that prints the first character and the last character of a string together
"""string=input("Enter a String")
result=string[0] + string[-1]
print(result)"""
#Ex6:Write a program that removes the first and last character of a string.
"""text=input("Enter string")
print(text[1:-1])"""
#Ex7:Write a program that removes the first and last character of a string.
"""text=input("Enter String")
print(text[::-1])"""
#Ex8:WAP to swip the first and last character
"""text = input("Enter String: ")
result = text[-1] + text[1:-1] + text[0]
print(result)"""
#Ex9:Write a program that prints:
#Characters at even indices
#Characters at odd indices
"""text = input("Enter String: ")
print("Even Index:", text[::2])
print("Odd Index :", text[1::2])
"""
#  *****Length Function **********
#Ex1:WAP to take string and find it's length
"""string=input("Enter String")
print(len(string))"""
#Ex2:Write a program to check whether the length of a string is even or odd.
"""string=input("Enter a String")
print (len(string))
if len(string) % 2 == 0:
    print("Length of string is Even")
else:
    print("Length of string is odd")
"""
#Ex3:Write a program to print the middle character of a string.
"""text = input("Enter String: ")
mid = len(text) // 2
print("Middle Character:", text[mid])
"""
#Ex4:Write a program to print stars (*) equal to the length of the entered string
"""string=input("Enter String")
print("*" * len(string))"""

#Ex5:WAP that accepts two strings and prints which one is longer. If both have the same length, print "Equal Length".
"""str1=input("Enter 1st string")
str2=input("Enter 2nd string")
if (len(str1)> len(str2)):
    print(str1,"is largest")
elif (len(str2)> len(str1)):
    print(str2,"is largest")
else:
    print("both are equal")"""
#************ Capitalization Function *********************
#Ex1: WAP to take string and capitilize it's first letter
"""string =input("Enter String")
print(string.capitalize())"""
#Ex2:Write a program that converts the first letter of every word into uppercase
"""string=input("Enter a string")
print(string.title())"""
#Ex3:Write a program that converts all characters of a string to uppercase.
"""string=input("Enter String")
print(string.upper())"""
#Ex4:Write a program that converts all characters of a string to lowercase.
"""string=input("Enter String")
print(string.lower())"""
#Ex5:Write a program that changes all uppercase letters to lowercase and all lowercase letters to uppercase.
"""string=input("Enter a String")
print(string.swapcase())"""

#*********  MIX QUESTION ************
#Question 1: Student Identity Card 
#Write a Python program that:
#Takes the student's first name and last name.
#Prints the full name in title case.
#Creates a username using the first 3 letters of the first name and the last 3 letters of the last name.
#Prints the total number of characters in the full name (excluding the space).
"""first_Name=input("Enter first Name")
last_Name=input("Enter Last Name")
full_name=first_Name.title()+ " " + last_Name.title()
print("FULL NAME: " , full_name)
user_name=first_Name[:3] + last_Name[-3:]
print("User Name:",user_name)
total_word=len(first_Name) + len(last_Name)
print("Total Word:",total_word)"""
#*************************************************************************************************
#Mirror Password
#Write a program that:
#Takes a password.
#Prints the password in uppercase.
#Creates a mirror password by joining the original password with its reverse.
#Prints stars (*) equal to the length of the password.
"""password=input("Enter password")
print("Password",password.upper())
mirror=password + password[::-1]
print("Mirror",mirror)
print("*" *len(password))"""
#***********************************************************************************************
#Write a program that:
#Takes a user's name.
#Capitalizes the first letter.
#Prints a line of = equal to the length of the message "Welcome " + name.
#Prints the welcome message.
#Prints the same line again.
"""user_name=input("Enter UserName")
message=("Well Come"+user_name.title())
line="="*len(user_name)
print(line)
print(message)
print(line)"""
#**********************************************************************************************
#Takes a word.
#Creates a secret code by joining:
#the last 2 characters,
#the middle part,
#the first 2 characters.
#Prints the code in uppercase.
"""word=input("Enter a Word")
code=word[-2:] + word[2:2] + word[:2]
print("Secret Code =",code.upper())"""
#********************************************************************************************
#Takes a full name.
#Prints:
#First character
#Last character
#Reverse of the name
#Length of the name
#Name in title case
"""full_name=input("Enter Your Full Name")
print("First Character",full_name[0])
print("Last Character",full_name[-1])
print("Reversre",full_name[::-1])
print("length",len(full_name))
print("Title",full_name.title())"""
