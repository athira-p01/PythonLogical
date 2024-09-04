x = int(input("Enter a number :"))
a = str(x)
sum = 0
for i in range(len(a)):
    res = int(a[i])
    sum = sum + res ** (i+1)
print(sum)

