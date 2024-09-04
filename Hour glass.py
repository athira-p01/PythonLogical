# for row in range(8):
#     for col in range(8):
#         if row==0 or col==0 or (col==0 and col==7) or (row==2 and col==6) or (row==3 and col==5):
#             print("*", end = " ")
#         else:
#             print(end = "  ")


# row == 5
# for j in range(0, 2, -1):
#     print("*", end = " ")
#     for j in range()


# a = str(input("enter 1st variable :"))
# b = str(input("enter 2nd variable :"))
# c=a
# a=b
# b=c
# if a and b and c:
#     print("true")
# else:
#     print("false")


word1 = input("enter a string:")
word2 = input("enter a string:")

if sorted(word1) == sorted(word2) or len(word1) == len(word2):
    print("True")
else:
    print("False")