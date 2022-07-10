x, y, x1, y1, x2, y2, r, s = tuple(map(float, input().split()))

in_rectangle = (x1 <= x <= x2 and y1 <= y <= y2)
in_circle = (x**2 + y**2 <= r**2)

if s == 0:
    print(in_rectangle or in_circle)
elif s == 1:
    print(in_rectangle and in_circle)
