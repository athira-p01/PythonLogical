n= int(input("Enter the no.of rows : "))
for i in range(n):
    count = 0
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
        if count < i:
            print("A", end="")
            count = count + 1
    print()
