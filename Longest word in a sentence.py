str = "Welcome to python programming"
str1 = str.split(" ")
count = 0
long = " "
for i in str1:
    if len(i) > count:
        count = len(i)
        long = i
print(long)

