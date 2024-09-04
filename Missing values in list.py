num = [1, 5, 7, 8]
num1 = []
for i in range(1, max(num)):
    if i not in num:
        num1.append(i)
print(num1)
