import sys

abc = [int(x) for x in sys.stdin.readline().split()]
abc.sort()
if abc == [5, 5, 7]:
    print("YES")
else:
    print("NO")
