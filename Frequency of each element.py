lis = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
freq = {}
for item in lis:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print(freq)