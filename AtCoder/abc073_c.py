import sys

n = int(sys.stdin.readline())
a_list = [int(x) for x in sys.stdin.readlines()]
a_list_index = list(set(a_list))
count = 0
for i in a_list_index:
    if a_list.count(i) % 2 == 0:
        continue
    else:
        count += 1

print(count)
