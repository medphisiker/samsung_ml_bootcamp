inp = input()

res = {}
max_item = 0
for i in range(len(inp) - 1):
    pair = inp[i:i+2]
    if pair not in res:
        res[pair] = 1
    else:
        res[pair] += 1

pairs = sorted(res.items(), key=lambda x: (x[1], x[0]), reverse=True)
print(pairs[0][0])
