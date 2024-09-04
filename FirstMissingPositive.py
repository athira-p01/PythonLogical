num = int(input("enter the number of elements: "))
num1 = []
for i in range(num):
    y = int(input("enter the values:"))
    num1.append(y)
print(num1)
# num = [1,9,8,5,4]
for i in range(1,max(num1)):
    if i not in num1:
        print(i)
        break