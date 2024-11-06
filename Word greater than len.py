s = "hello geeks for geeks is computer science portal"
k = 4
words = s.split()
result = ""
for i in words:
    if len(i) > k:
        result += i + " "
print(result)
