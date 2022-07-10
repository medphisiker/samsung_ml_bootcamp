inp = input()[::-1]

res = []
for i in range(len(inp) - 1):
    if 'a' in inp[i]:
        res.append(inp[i:i+2])

print(len(res))
