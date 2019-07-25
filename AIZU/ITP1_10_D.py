import sys

N = int(sys.stdin.readline())
xList = [int(x) for x in sys.stdin.readline().split()]
yList = [int(x) for x in sys.stdin.readline().split()]
pList = [0, 0, 0, 0]

for i in range(N):
    dif = abs(xList[i] - yList[i])
    pList[0] += dif
    pList[1] += dif ** 2
    pList[2] += dif ** 3
    if pList[3] < dif:
        pList[3] = dif
pList[1] = pList[1] ** (1 / 2)
pList[2] = pList[2] ** (1 / 3)
for i in pList:
    print(i)
