n = int(input("Enter a number: "))
x = 0
y = 1
while y < n:
    x = y
    y = x + y
if y == n:
    print(f"{n} is a Fibonacci number")
else:
    print(f"{n} is not a Fibonacci number")
