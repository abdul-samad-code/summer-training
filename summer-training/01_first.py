#Python :- Python ek high-level, interpreted, general-purpose programming language hai.
#Example:-
print("hello world")
print(10)
print("samad",22,"lucknow")
print("===================Variables===============================")

# This is comment     (single line comment)
"""
This is 
multi line
commeent
"""


#Variables
name = "abdul samad"
age = 21
age = 22
height = 7.7
print(name)
print(age)
print(height)
print("======================Data Types============================")



"""
variable naming rules
Correct :-  name, user_name, student12, _age
incorrect:-  1name, my-name, class
"""


# Data Types
# integer
age = 21
print(type(age))
# Float
price = 25.99
print(type(price))
# String 
name = "string"
print(type(name))
# Boolean
is_student = True
print(type(is_student))
print("==================Input================================")


# Input     (input always return string)
name = input("Enter your name: ")
print(name)
print("=================Type Casting=================================")


# Type Casting
age = "77"
age = int(age)
print(age)

price = "45.6"
price = float(price)
print(price)

roll_no = 30
print(str(roll_no))
print("===================Multiple Assignment===============================")

# Basic operation
#addition   10 + 5
#subtraction 10 - 4
#multiplication  10 * 6
#division   10/2
#floor division  10 // 7
#modulus  10 % 3
#exponent 2**3

# Multiple Assignment
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)
print("_________________swap variables________________________")


#Swap variables
a = 40
b = 60
a,b = b,a
print(a)
print(b)
print("___________________F-String____________________________")


# Constant (Convention)
#PI = 3.14159
#MAX_SIZE = 100



#  F-String
name = "abdul"
age = 41
print(f"My name is {name} and I am {age} years old.")
print("______________________________________________________")












