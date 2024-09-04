# 1.Function without argument with return values
def sum():
    a = 10
    b = 20
    c = a+b
    print(c)
sum()


# 2.Function with argument without return values
def sum(x,y):
    c = x+y
    print(c)
sum(10,20)


# 3.Function with argument with return values
def sum(x,y):
    c = x+y
    return c
x1 = sum(10,20)
print(x1)


# 4.Function without argument with return values
def sum():
    x = 10
    y = 20
    z = x+y
    return z
x1 = sum()
print(x1)
