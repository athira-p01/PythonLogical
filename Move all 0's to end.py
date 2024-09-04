lis = [1, 0, 2, 3, 0, 4, 0, 5]
zeros = []
xy = []
for i in range(len(lis)):
    if lis[i] == 0:
        zeros.append(lis[i])
    else:
        xy.append(lis[i])
print(xy + zeros)
