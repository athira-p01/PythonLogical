# # Hollow Heart Shape
# for row in range(6):
#     for col in range(7):
#         if (row == 0 and (col == 1 or col == 2 or col == 4 or col == 5) or
#             row == 1 and (col == 0 or col == 3 or col == 6) or row == 2 and (col == 0 or col == 6) or
#             row == 3 and (col == 1 or col == 5) or row == 4 and (col == 2 or col == 4) or row == 5 and col == 3):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()





## Star fill in the Heart Shape
# for row in range(6):
#     for col in range(7):
#         if (row == 0 and (col == 1 or col == 2 or col == 4 or col == 5) or
#             row == 1 or row == 2 or
#             row == 3 and (col == 1 or col == 2 or col == 3 or col == 4 or col == 5) or
#             row == 4 and (col == 2 or col == 3 or col == 4) or row == 5 and col == 3):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()





# Names in the center of heart shape
num = int(input("Enter the number: "))
msg = input("Enter any msg: ")
l = len(msg)
n = num // 2

for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1), end="" )

    if num % 2 == 0:
        for j in range(2 * (n - i - 1)):
            print(" ", end="")
        print("* " * (i + 1), end="")
    else:
        for j in range(2 * (n - i - 1) + 1):
            print(" ", end="")
        print("* " * (i + 1), end="")

    print()

if num % 2 == 0:
    print("* " * ((num - 1) // 2) + " ".join(msg) + " *" * ((num - 1) // 2))
else:
    print("* " * ((num - 1) // 2) + " ".join(msg) + " *" * (((num - 1) // 2) + 1))

for i in range(num, 0, -1):
    print(" " * (num - i) + "* " * i)
