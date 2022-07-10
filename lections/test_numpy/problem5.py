import numpy as np
import sys

# считываем матрицу
a = []
for line in sys.stdin:
    s = line.strip()
    if s:
        a.append([float(i) for i in s.split()])
    else:
        break


a = np.array(a)
mean = np.mean(a, axis=1)

for row_i in range(a.shape[0]):
    a[row_i] -= mean[row_i]

print(a)
