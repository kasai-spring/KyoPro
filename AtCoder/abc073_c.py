import sys
import collections

n = int(sys.stdin.readline())
a_list = [int(x) for x in sys.stdin.readlines()]
a_list_counter = collections.Counter(a_list)
count = 0
for i in a_list_counter:
    if a_list_counter[i] % 2 != 0:
        count += 1
    else:
        continue
print(count)
