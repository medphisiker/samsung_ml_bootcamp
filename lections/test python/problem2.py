ex = [2, 3, 4, 5, 2, 5, 4, 3, 2, 3, 8, 5, 6]

arr = [[i]*i for i in ex if i % 2 == 0]
print(arr)
