def function_name():
    print("function executes")
function_name()

print("________________fun with parameters___________________________________")

def greet(name):
    print("hello", name)
greet("samad")

print("_________________with multiple parameters___________________________________")

def add(a, b):
    print(a+b)
add(3,4)

print("________________fun returning a value_______________________________")

def adding(a, b):
    return a+b
result = adding(55,66)
print(result)

print("________________fun with default parameters __________________________")

def greeting(name="samad"):
    print("hello", name)
greeting()
greeting("abdul")