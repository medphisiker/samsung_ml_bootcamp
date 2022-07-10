import numpy as np

x = [1, 1, 2, 5, 6, 7, 3, 4, 5, 6]


print(np.mean(x))
print(np.var(x))
print(np.std(x))

x1 = [1, 5, 6, 2, 8, 4, 3]
x2 = [545, 546, 550, 544, 548, 547, 543]
print(np.var(x1) - np.var(x2))

x1 = [3, 5, 3, 6, 7, 2, 1, 0, 15, 4]
x2 = [-3, -2, 6, 8, 4, 1, 0, 8, 2, 8]
print(np.corrcoef(x1, x2))
