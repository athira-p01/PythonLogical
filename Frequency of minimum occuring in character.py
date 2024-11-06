# str = input("Enter a string : ")
str = "aabbbcccc"
count = {}
for char in str:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
freq = min(count.values())
print(freq)

