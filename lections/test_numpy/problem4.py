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


a = np.array(a).max(axis=0)
print(len(a[a == 0]))
