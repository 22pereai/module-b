# calc.py
# Aidan Perez 5/1/19
# Does mathematical equations.

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("This is calc.py. it runs mathetmatical equations.")
for i in range(10000):
    x = eval(input("Please input the 1st number. "))
    y = eval(input("Please input the 2nd number. "))
    z = eval(input("1. Addition, 2. Subtraction, 3. Multiplication, 4. Division. "))
    if z == 1:
        print(add(x, y))
    elif z == 2:
        print(sub(x, y))
    elif z == 3:
        print(mul(x, y))
    elif z == 4:
        print(div(x, y))
    else:
        print("That is not 1 through 4.")
        break