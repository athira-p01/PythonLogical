s = "GeeksforGeeks"
leastchar = None
leastcount = len(s) + 1
for char in s:
    count = 0
    for i in s:
        if i == char:
            count += 1
    if count < leastcount:
        leastcount = count
        leastchar = char
print("The minimum of all characters in", s, "is:", leastchar)
