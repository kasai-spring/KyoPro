n = int(input())
v_list = [int(x) for x in input().split()]
v_list.sort()
while len(v_list) > 1:
    a = v_list.pop(0)
    b = v_list.pop(0)
    v_list.insert(0, (a + b) / 2)
print(v_list[0])
