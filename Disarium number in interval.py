for j in range(1, 101):
    a = str(j)
    sum = 0
    for i in range(len(a)):
        res = int(a[i])
        sum = sum + res ** (i+1)
    if sum == j:
        print(j)

