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