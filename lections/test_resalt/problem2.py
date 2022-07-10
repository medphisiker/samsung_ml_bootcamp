import numpy as np
import sys

# считываем размер k
k = int(input())

# считываем матрицу
a = []
for line in sys.stdin:
    s = line.strip()
    if s:
        a.append([int(i) for i in s.split()])
    else:
        break

a = np.array(a)
n, m = a.shape
new_arr = []

for i in range(0, n, k):
    tmp_lst = []
    for j in range(0, m, k):
        block = a[i:i + k, j:j + k]
        tmp_lst.append(block.sum())

    new_arr.append(tmp_lst)

for row_i in new_arr:
    print(" ".join(str(i) for i in row_i))
