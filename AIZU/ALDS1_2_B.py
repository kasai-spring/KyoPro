import sys

N = int(sys.stdin.readline())
nList = [int(x) for x in sys.stdin.readline().split()]
count = 0
for i in range(N):
    minJ = i
    for j in range(i, N):
        if nList[minJ] > nList[j]:
            minJ = j
    if minJ == i:
        continue
    else:
        nList[i], nList[minJ] = nList[minJ], nList[i]
        count += 1
print(" ".join(map(str, nList)))
print(count)
