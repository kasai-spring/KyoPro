import sys

n = int(sys.stdin.readline())
a_list = [int(x) for x in sys.stdin.readline().split()]
b_list = [int(x) for x in sys.stdin.readline().split()]
result = 0
for i in range(n):
    if b_list[i] <= a_list[i]:
        result += b_list[i]
    else:
        result += a_list[i]
        b_list[i] -= a_list[i]
        if b_list[i] <= a_list[i + 1]:
            a_list[i + 1] -= b_list[i]
            result += b_list[i]
        else:
            result += a_list[i + 1]
            a_list[i + 1] = 0
print(result)