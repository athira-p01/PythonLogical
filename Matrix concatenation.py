import numpy as np
x = np.matrix([[1,2],[3,4]])
y = np.matrix([[5,6]])
res = np.concatenate((x,y))
print(res)



# List concatenation
A = [[1,2,3],[4,5,6]]
B = [[2,4,6],[1,3,5]]
result = A + B
print(result)
