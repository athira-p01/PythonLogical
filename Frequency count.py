# list = [1,2,3,4,3,4,5,4,6,7,8,9]
# freq = list.count(4)
# print(freq)



x = int(input("Enter a limit :"))
y = []
count = 0
target = 2
for i in range(x):
    a = int(input("Enter the values :"))
    y.append(a)
print(y)
for j in y:
    if j == target:
        count = count+1
print(count)



