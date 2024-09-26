# num = 5
# start = 15
# for i in range(1, num + 1):
#     val = start
#     diff = num - 1
#     for j in range(i):
#         print(val, end=" ")
#         val -= diff
#         diff -= 1
#     start -= 1
#     print()




num = 5
start = 15
for i in range(1, num+1):
    for j in range(i):
        print(start, end="  ")
        start -= 1
    print()
