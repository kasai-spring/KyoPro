n = int(input())
a_list = [int(x) for x in input().split()]
a_list.sort(reverse=True)
A, B = 0, 0
for i in range(len(a_list)):
    if i % 2 == 0:
        A += a_list[i]
    else:
        B += a_list[i]
print(A - B)
