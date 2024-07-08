num = int(input("enter a number :"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print("factorial of",num,"is",fact)


# num = int(input("enter a number :"))
# fact = 1
# if num < 0:
#     print("factorial doesn't exist for negative numbers")
# elif num == 0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         fact = fact * i
# print("factorial of", num ,"is", fact)