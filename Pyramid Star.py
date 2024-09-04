## Star pattern in right angled triangle
# n = int(input("Enter no.of rows: "))
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()



## Star pattern in odd right angled triangle
# n = int(input("Enter no.of rows: "))
# for i in range(1, n+1):
#     for j in range(1, 2*i):
#         print("*", end=" ")
#     print()



## Star pattern in pyramid shape
n = int(input("Enter no.of rows: "))
for i in range(n):
    for j in range(n, i, -1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()