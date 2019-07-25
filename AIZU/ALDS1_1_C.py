import sys
import math

count = 0
listA = [int(x) for x in sys.stdin.readlines()]  #
for i in listA:
    if i == 1:
        count += 1
        continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        count += 1
print(count)
