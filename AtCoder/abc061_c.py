import sys

n, k = (int(x) for x in sys.stdin.readline().split())
a_b_list = [[int(x) for x in sys.stdin.readline().split()] for y in range(n)]
a_b_list.sort(key=lambda x: x[0])
total_index = 0
for i in a_b_list:
    total_index += i[1]
for i in reversed(a_b_list):
    start = total_index
    end = total_index - i[1] + 1
    if start >= k >= end:
        print(i[0])
        sys.exit(0)
    total_index -= i[1]
