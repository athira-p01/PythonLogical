list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
combined = list(zip(list2, list1))
combined.sort()
sorted = []
for i in combined:
    sorted.append(i[1])
print(sorted)
