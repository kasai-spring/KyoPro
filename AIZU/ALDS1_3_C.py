import sys
from collections import deque

N = int(sys.stdin.readline())
resultList = deque()
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "insert":
        resultList.appendleft(command[1])
    elif command[0] == "delete":
        try:
            resultList.remove(command[1])
        except:
            pass
    elif command[0] == "deleteFirst":
        resultList.popleft()
    else:
        resultList.pop()
print(" ".join(resultList))
