import numpy as np
import sys


a = set()
for line in sys.stdin:
    s = line.strip()
    if len(s):
        a.add("".join(s))
    else:
        break

print(len(a))
