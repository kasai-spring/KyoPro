import sys

N = int(sys.stdin.readline())
aList = [int(x) for x in sys.stdin.readline().split()]
for i in range(N):
    compare = aList[i]
    for j in range(i + 1):
        if aList[j] > compare:
            del aList[i]
            aList.insert(j, compare)
            break

    print(" ".join(map(str, aList)))
