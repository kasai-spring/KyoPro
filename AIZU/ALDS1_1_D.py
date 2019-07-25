import sys

N = int(sys.stdin.readline())
listA = [int(x) for x in sys.stdin.readlines()]
minN = listA[0]
maxT = listA[1] - listA[0]
del listA[0]
for i in listA:
    diff = i - minN
    if diff > maxT:
        maxT = diff
    if minN > i:
        minN = i
print(maxT)
