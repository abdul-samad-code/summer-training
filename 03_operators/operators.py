#  Comparison Operators

"""
==  equal        a==b
!=  NOt equal    a!=b
>   Greater than a>b
<   less than    a<b
<=
>=
"""

# example
x = 10
y = 20
print(x==y)
print(x!=y)
print(x<y)
print(x>=y)
print("___________________________________________________")


# Logical operations

#AND operator
age = 20 
citizen = True
if age >= 18 and citizen:
    print("Eligible")

# OR operator
mark = 85
sport = True
if mark >= 90 or sport:
    print("selected")

# NOT operator
logged_in = False
if not logged_in:
    print("Please login ")

print("_________________________________________________________")

# Ternery operator
age = 20
result = "abdul" if age >= 18 else "Minor"
print(result)
