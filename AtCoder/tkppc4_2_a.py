x, y = (int(x) for x in input().split())
if x % 2 == 0:
    if abs(x) * 2 <= y and y % 4 == 0:
        print(int(abs(y / 2)))
    else:
        print(-1)
else:
    if abs(x) * 2 <= y and (y + 2) % 4 == 0:
        print(int(abs(y / 2)))
    else:
        print(-1)
