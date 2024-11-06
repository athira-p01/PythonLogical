A = "apple banana mango"
B = "banana fruits mango"
words = (A + " " + B).split()
new = []
for i in words:
    if words.count(i) == 1:
        new.append(i)

print(new)
