import sys

x, y = (int(x) for x in sys.stdin.readline().split())
if y > x:  # swap
    x, y = y, x
while y > 0:
    r = x % y
    x = y
    y = r
print(x)
