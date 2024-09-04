def sum(x,y):
    c = x+y
    return c
def difference(x,y):
    c = x-y
    return c
def multiplication(x,y):
    c = x*y
    return c
def division(x,y):
    c = x/y
    return c

print("Enter choice:")
print("1.sum")
print("2.difference")
print("3.multiplication")
print("4.division")

while True:
    select = int(input("Select a choice :"))
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    if select == 1:
       print(num1,"+",num2,"=", sum(num1,num2))
    elif select == 2:
       print(num1,"-",num2,"=", difference(num1,num2))
    elif select == 3:
       print(num1, "*", num2, "=", multiplication(num1, num2))
    elif select == 4:
       print(num1,"/",num2,"=", division(num1,num2))
    else:
       print("Invalid output")
