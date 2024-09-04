# x = [1,2,3,4,5]
# avg = sum(x) / len(x)
# print(avg)

x = [1,2,3,4,5]
sum = 0
for i in x:
    sum = sum+i
avg = sum / len(x)
print("The average of list is :",avg)