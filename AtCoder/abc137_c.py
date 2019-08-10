import sys
from collections import Counter
import math

N = int(sys.stdin.readline())
s_list = ["".join(sorted(list(sys.stdin.readline().rstrip()))) for x in range(N)]
s_list = Counter(s_list)
count = 0
for i in s_list.values():
    if i == 1:
        continue
    count += (math.factorial(i) // math.factorial(i - 2)) // math.factorial(2)
print(count)
