lis1 = [1, 2, 4, 6, 7, 8]
n = int(input("Enter the no.of times to left rotate : "))
lis2 = lis1[n:] + lis1[:n]
print("Original list : ", lis1)
print("List after left rotate : ",lis2)
