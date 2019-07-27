import sys

n = int(sys.stdin.readline())
p_list = [int(x) for x in sys.stdin.readline().split()]
p_list_sort = sorted(p_list)
if p_list == p_list_sort:
    print("YES")
    sys.exit(0)
for i in range(len(p_list)):
    for j in range(len(p_list)):
        if i == j:
            break
        p_list[i], p_list[j] = p_list[j], p_list[i]
        if p_list == p_list_sort:
            print("YES")
            sys.exit(0)
        else:
            p_list[i], p_list[j] = p_list[j], p_list[i]
else:
    print("NO")
