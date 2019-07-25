import sys

count = 0
N = int(sys.stdin.readline())
nList = [int(x) for x in sys.stdin.readline().split()]
while True:
    changeStatus = True
    for i in reversed(range(N)):
        if i == 0:
            break
        if nList[i] < nList[i - 1]:
            count += 1
            nList[i], nList[i - 1] = nList[i - 1], nList[i]
            changeStatus = False
    if changeStatus:
        break

print(" ".join(map(str, nList)))
print(count)
