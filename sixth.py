#**********************   TUPLE **************************
#Ex1:
"""tuple1 = (1,2,3,4,5,8,9,9,0,11,)
for i in tuple1:
    print(i)"""
#Ex2: joining Tuples
"""tuple1= (1,2,3,4,5)
tuple2= (6,7,8,9,10)
tuple3 = tuple1 + tuple2
print(tuple3)"""
#Ex3: Input Element From User ........
"""a = ()
size = int(input("Enter Size of tuples"))
for i in range(size):
    num=int(input("Enter Tuples Element"))
    a = a+ (num,)
print("Tuples", a)"""
#Ex4:Replicating Tuples
"""t1=("Hello, ")
t2= t1 * 3
print(t2)"""
#***************************************
"""tup=("orange","apple","banana")
y=list(tup)
y[2]="Cherry"
tup=tuple(y)
print(tup)"""
#       DELETION  OF TUPLE 
"""tup=("orange","apple","banana")
#
print(tup)
del(tup)
print(tup)"""
#      LEN () IN TUPPLE
"""tup=("orange","apple","banana")
print(len(tup))"""
#      MAX () IN TUPPLE
"""tup=[12,34,7,5,3,89,76,5]
print(max(tup))"""
#      MIN () IN TUPPLE
"""tup=[12,34,7,5,3,89,76,5]
print(min(tup))"""  
#      INDEX IN TUPPLE
"""tup=[12,34,7,5,3,89,76,5]
print(tup.index(89))
"""
#       COUNT IN TUPPLE
"""tup=[12,34,3,5,3,89,76,5,3,3]
x=tup.count(3)
print(x)"""

#       ITEM EXIST OR NOT
"""t=("a","b","c","d")
del(t)
print(t)"""
#               MIX PROGRAM ON TUPPLES  
#Ex1:
# Write a program to take n integers from the user, store them in a tuple, and count the number of even and odd elements.
"""a = ()
size = int(input("Enter Size of tuples"))
for i in range(size):
    num=int(input("Enter Tuples Element"))
    a= a+ (num,)
even = 0
odd = 0
for num in a:
    if num % 2 == 0:
        even = even +1
    else:
        odd=odd+1
print("Tuples",a)
print("Odd ",odd)
print("Even ", even)"""

#Ex2:Write a program to find the second largest element in a tuple
"""a = ()
size = int(input("Enter Size Of Tupples"))
for i in range(size):
    num=int(input("Enter Element of Tuple"))
    a=a+ (num ,)
largest = max(a)
second = a[0]

for i in a:
    if i != largest and i > second:
        second = i
print("1st Largest " , largest)
print("2nd largest ",second)"""

"""a = ()
size = int(input("Enter Size Of Tupples"))
for i in range(size):
    num=int(input("Enter Element of Tuple"))
    a=a+ (num ,)
search=int(input("Enter the element to search"))
if search in a:
    print("Found")
else:
    print("Not FOund")"""