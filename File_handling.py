# ALL ABOUT FILE HANDLING
    # ****(1)****

# HOW TO Create FILE .....
# f=open("C:\\Users\\Officer Danyal\\Desktop\\python\empty.txt","w")
# print("File Created Successfully ! ")
 
    # ****(2)****

# HOW TO Write FILE .....
# f=open("C:\\Users\\Officer Danyal\\Desktop\\python\\empty.txt","w")
# f.write("This is FIle Handling in Python  ")
# print("File Created Successfully ! ")
    # ****(3)****

# How TO Read   File .....
# f=open("C:\\Users\\Officer Danyal\\Desktop\\python\\empty.txt","r")
# print(f.read(30))
# print("File Read Successfully ! ")

    # ****(4)****


# How To Delete Files ...........
# import os
# if os .path.exists("C:\\Users\\Officer Danyal\\Desktop\\python\empty.txt"):
#     os.remove("C:\\Users\\Officer Danyal\\Desktop\\python\empty.txt")

     # ****(5)****
# Create and Write Employee Records
# file = open("employee.txt", "w")
# for i in range(3):
#     name = input("Enter Employee Name: ")
#     salary = input("Enter Salary: ")
#     file.write(f"{name} - {salary}\n")
# file.close()
# print("Employee records saved successfully.")

     # ****(6)****
Delete a File Safely
import os
file_name = input("Enter The Name Of File You Want To Delete :")
try:
    os.remove(file_name)
    print("Files Deleted Successfully ")
except FileNotFoundError:
    print("File Not Found ")
except PermissionError:
    print("Permission Denied")
except Exception as e:
    print(e)


