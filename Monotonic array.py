A = [6, 5, 4, 4]
n = len(A)
increasing = True
decreasing = True
for i in range(1, n):
    if A[i] < A[i - 1]:
        increasing = False
    if A[i] > A[i - 1]:
        decreasing = False

if increasing or decreasing:
    print("Monotonic")
else:
    print("Not monotonic")

