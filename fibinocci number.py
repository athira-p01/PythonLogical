# n = int(input("enter a number :"))
# a=0
# b=1
# if n==1:
#     print(a)
# else:
#     for i in range(2,n+1):
#         c=a+b
#         a=b
#         b=c
#     print(b)


n = int(input("Enter a positive integer N: "))
a = 0
b = 1
for i in range(2, n + 1):
    next_term = a + b
    a = b
    b = next_term
print(a)