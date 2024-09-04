n = int(input("Enter a number :"))
x = n
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
if x % sum == 0:
    print(x, "is a Harshad number")
else:
    print(x, "is not Harshad number")
