day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:                   # it is defaut case in case if not match any case this case defaulty print msg (  _ mendatory for default case)
        print("Invalid")


print("______________________________________________________")


# Truth and Falsy value
"""
falsy:
 False
 0
 0.0
 ""
 []
 {}
 ()
 None
 """

# example 

name = ""
if name:
    print("Name found")
else:
    print("Name is Empty")