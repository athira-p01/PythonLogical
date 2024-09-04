x = [8,9,1,2,5,5]
target = 10
count = 0
for i in range(len(x)):
    for j in range(i+1, len(x)):
        if x[i] + x[j] == target:
            count = count+1
print(count)
