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
"""first_name=input("Enter Your First Name")
last_name=input("Enter Your Last Name")
full_name=first_name + last_name
print("Your Full Name is:",3*full_name)"""
#Ex3:STRING SLICING :) Write a program that prints the first 4 characters of a string.
"""string=input("Enter A String")
print(string[0:5])"""
#Ex4:STRING SLICING :) Write a program that prints the last 3 characters of a string
"""string=input("Enter A String")
print(string[-3:])"""
#Ex5:STRING SLICING :) Write a program that prints the first character and the last character of a string together
"""string=input("Enter a String")
result=string[0] + string[-1]
print(result)"""
#Ex6: Length Function:)WAP to take string and find it's length
"""string=input("Enter String")
print(len(string))"""
#Ex7:Capitalization Function:) WAP to take string and capitilize it's first letter
"""string =input("Enter String")
print(string.capitalize())"""