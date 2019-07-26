import sys
a, b = (int(x) for x in sys.stdin.readline().split())
if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
