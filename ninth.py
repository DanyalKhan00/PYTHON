# ************ ALL ABOUT SET *************************
# my_set = {"dani","aimi","zarar","saad"}
# print(type(my_set))

# *** Create A set with Different Data type ***

# my_set={"Dani", 12, 34.5 ,True}
# print(my_set)

# *** Printing Set Through Loop
# my_set = {"Dani", 12, 34.5 ,True,"Aimi","Emo"}
# for i in my_set:
#     print(i)


# *** Length of  Set ***
# my_set = {"Dani", 12, 34.5 ,True,"Aimi","Emo"}   
# print(len(my_set))    


# *** Adding item to set ***
# my_set = {"Dani", 12, 34.5 ,True,"Aimi","Emo"}
# my_set.add("Samar")
# print(my_set)



# ***  Remove item From Set ***
# my_set = {"Dani", 12, 34.5 ,True,"Aimi","Emo"}
# my_set.remove(12)
# print(my_set)

# ***  Clear the set ***
# my_set = {"Dani","Dani" ,12, 34.5,12 ,True,"Aimi","Emo"}
# print(my_set.clear)

# ***   Delete the entire Set ***
# my_set = {"Dani", 12, 34.5 ,True,"Aimi","Emo"}
# del my_set

# *** Joining Two Set ***

# my_set1 = {"Dani", 12, 34.5}
# print(my_set1)
# my_set2 = {True,"Aimi","Emo"}
# print(my_set2)
# my_set1.update(my_set2)
# print(my_set1)


# *** Difference Between Two Sets
# my_set1 = {"Dani", 12, 34.5}
# my_set2 = {True,"Aimi","Emo","Dani"}
# res= my_set1.difference(my_set2)
# print(res)

# *** Copy Of A Set ***
# my_set = {True,"Aimi","Emo","Dani"}
# print(my_set)
# res = my_set.copy()
# print(res)


# *** PRACTICE QUESTION ON PYTHON ***
#Q1:Write a Python program to take two sets from the user and print the common elements.
"""s1 = set()
s2 = set()
size1=int(input("Enter Size 1: "))
for i in range(size1):
    num = int(input("Enter S1 Element: "))
    s1.add(num)

size2=int(input("Enter Size 2: "))
for i in range(size2):
    num = int(input("Enter S2 Element: "))
    s2.add(num)
common = s1.intersection(s2)
print("Commone Element : ", common)"""

# #Q3:Write a Python program to create a set from user input and count how many even and odd numbers are present.
# s1 = set()
# size= int(input("Enter Size : "))
# for i in range(size):
#     num=int(input("Enter Element : "))
#     s1.add(num)
# odd = 0
# even = 0
# for num in s1:
#     if num % 2 == 0:
#         even =even  + 1
#     else:
#         odd = odd + 1
# print("Even : ",even)
# print("Odd : ", odd)
