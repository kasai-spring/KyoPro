import sys

n, y = (int(x) for x in input().split())
for i in range(n + 1):
    for j in range(n + 1 - i):
        if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            print(str(i) + " " + str(j) + " " + str(n - i - j))
            sys.exit(0)
else:
    print("-1 -1 -1")
