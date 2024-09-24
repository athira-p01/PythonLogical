# num = 5
# for i in range(1, num + 1):
#     val = i
#     diff = num - 1
#     for j in range(i):
#         print(val, end=" ")
#         val += diff
#         diff -= 1
#     print()


n = int(input(" Enter the no.of row : "))
for i in range(n):
    for j in range(i+1):
        x = 0
        for k in range(j):
            x = x+n-k
        if j % 2 == 0:
            print(x+i-j+1, end=" ")
        else:
            print(x+n-i, end=" ")
    print()
