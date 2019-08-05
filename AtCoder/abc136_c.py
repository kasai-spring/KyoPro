import sys

n = int(sys.stdin.readline())
h_list = [int(x) for x in sys.stdin.readline().split()]
h_list[0] -= 1
for i in range(len(h_list)):
    if i == 0:
        continue
    try:
        if h_list[i] > h_list[i - 1]:
            h_list[i] -= 1
        elif h_list[i] == h_list[i - 1]:
            continue
        elif h_list[i] < h_list[i - 1]:
            print("No")
            sys.exit(0)
    except IndexError:
        continue
else:
    print("Yes")
