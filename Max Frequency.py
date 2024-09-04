word_count = {"apple":4 , "banana":6 , "cherry":2}
max_value = " "
max_count = 0
for i,j in word_count.items():
    if max_count < j:
        max_value = i
        max_count = j

print(max_value)


