str = "Welcome to Python Programming"
spl = str.split(" ")
for i in spl:
    x1 = len(i)
    if x1 % 2 == 0:
        print(i)
