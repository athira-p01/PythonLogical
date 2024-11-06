# import numpy as np
# matrix = np.array([["Gfg", "good"], ["is", "for"]])
# res = np.hstack([matrix[0],matrix[1]])
# print(res)



matrix = [["How", "I"], ["are", "am"], ["you?", "good."]]
result = []
for i in range(len(matrix[0])):
    res = ""
    for j in matrix:
        res += j[i]
    result.append(res)
print(result)
