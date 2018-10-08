def add(a,b):
    c=a+b
    print("The sum is:",c)
    return c
def sub(a,b):
    c=a-b
    print("The difference is:",c)
    return c
def divide(a,b):
    c=a/b
    print("The division is:",c)
    return c
def mult(a,b):
    c=a*b
    print("The product is:",c)
    return c
def floatd(a,b):
    c=a//b
    print("The floatdivision is:",c)
    return c
def power(a,b):
    c=a**b
    print("The answer is:",c)
    return c
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Choose from the following options:\n 1-Addition\n 2-Subtraction\n 3-Division\n 4-Multiplication\n 5-FloatDivision\n 6-RaisedTo\n Your Choice:"))
if z==1:
    add(x,y)
elif z==2:
    sub(x,y)
elif z==3:
    divide(x,y)
elif z==4:
    mult(x,y)
elif z==5:
    floatd(x,y)
elif z==6:
    power(x,y)
else:
    print("you entered an invalid option.")
    

    
