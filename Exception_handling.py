# **** ALL ABOUT EXCEPTION HANDLING ****

#         (1)
# A = int(input("Enter 1st Number : "))
# B = int(input("Enter 2nd Number : "))
# try:

#     C = A/B

#     print("Result : ", C)
   
# except:
#      print("Can't Divide By Zero")



       # (2)
# try:
#     marks = []

#     for i in range(5):
#         mark = float(input(f"Enter marks of subject {i+1}: "))

#         if mark < 0 or mark > 100:
#             raise ValueError("Marks should be between 0 and 100.")

#         marks.append(mark)

#     average = sum(marks) / len(marks)
#     print("Average Marks =", average)

# except ValueError as e:
#     print(e)

# except Exception as e:
#     print(e)



#   (3)
# try:
#     numbers = []
#     for i in range(5):
#         numbers.append(int(input("Enter Number : ")))
#         index = int (input("Enter Index "))

#         print("Element =",numbers[index])
# except ValueError :
#     print("Please Enter Only Integer ")
# except IndexError:
#     print("invalid Index")
# except Exception as e:
#     print(e)



