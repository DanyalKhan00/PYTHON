# *************     DICITIONARY ********************
"""dict1 = {'brand':'suzuki','model':'dzir','year':'2020'}
print(dict1)"""

# ****************      
"""detail={'name':'dani','r_no':'250141','class':'CS'}
print(detail)
d=detail.get('class')
print(d)"""
# ACCESSING ELEMENT OF DICITIONARY *
"""x=dict1.get("year")
print(x)
y=dict["model"]
print(y)"""
# Accessing Element through Loop
"""dict1={'brand':'suzuki','model':'dzire','year':'2020'}
for i in dict1:
    print(i)"""  # this will print only key not values
"""
dict1={'brand':'suzuki','model':'dzire','year':'2020'}
for i in dict1:
    print(dict1[i])"""   # this will print only values not key
# ******** CHANGING DICTIONARY ELEMENT .....
"""dict1 = {'brand':'suzuki','model':'dzir','year':'2020'}
dict1['year']=2026
print(dict1)"""
# Chk Whether a key Exist or Not ....
"""dict1 = {'Brand' : 'Civic', 'model' : 'Honda', 'year':'2024'}
if 'Brand' in dict1:
    print("Yes Exist")
else:
    print("Not Exist")"""
# Adding New Element ...
"""dict1 = {'brand':'Honda','model':'civic','year':2027}
print(dict1)
dict1['color']='black'
print(dict1)"""
# FUNCTION IN DICIINARY
#1): LEN()
"""dict1 = {'brand':'Honda','model':'civic','year':2027}
print("lenght of Dict1",len(dict1)) """
#2): POP()
"""dict1={'brand':'honda','model':'civic','year':'2020'}
print(dict1.pop('model'))
print(dict1)"""
#3): POPITEM()
"""dict1={'brand':'honda','model':'civic','year':'2020'}
print(dict1.popitem())
print(dict1)"""
#4): DEL ()
"""dict1={'brand':'honda', 'model':'civic', 'year':'2029'}
print(dict1)
del dict1['model']
print(dict1)"""
#5) TO DELETE ENTIRE DICITIONARY
"""dict1={'brand':'honda', 'model':'civic', 'year':'2029'}
print(dict1)
del dict1
print(dict1)"""
#6): Clear Key Word
"""dict1={'brand':'honda', 'model':'civic', 'year':'2029'}
print(dict1)
dict1.clear()
print(dict1)"""

#7): Copy
"""dict1={'brand':'honda', 'model':'civic', 'year':'2029'}
print(dict1)
dict2=dict1.copy()
print(dict2)"""
#8): Update
"""dict1={'brand':'honda', 'model':'civic', 'year':'2029'}
print(dict1)
dict1.update({"color":"white"})
print(dict1)"""

