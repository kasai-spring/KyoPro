# todo time limit
import sys
from collections import deque

n, m = (int(x) for x in sys.stdin.readline().split())
a_b_list = [[int(x) for x in sys.stdin.readline().split()] for y in range(m)]
count = 0
for i in a_b_list:
    a, b = i[0], i[1]
    a_b_list_temp = [[x for x in y] for y in a_b_list]
    a_b_list_temp.remove([a, b])
    # aをスタートとし、bをゴールと仮定する
    q = deque([])
    for j in a_b_list_temp:
        if j[0] == a:
            q.append([a, j[1]])
        elif j[1] == a:
            q.append([a, j[0]])
    findRoot = False
    while len(q) > 0:
        a_b_root = q.pop()
        for j in a_b_list_temp:
            if (j[0] == a_b_root[-1] and j[1] == b) or (j[1] == a_b_root[-1] and j[0] == b):
                findRoot = True
                q.clear()
                break
            if a_b_root[-1] == j[0]:
                if j[1] not in a_b_root:
                    q.append(a_b_root + [j[1]])
            if a_b_root[-1] == j[1]:
                if j[0] not in a_b_root:
                    q.append(a_b_root + [j[0]])
    if not findRoot:
        count += 1

print(count)
