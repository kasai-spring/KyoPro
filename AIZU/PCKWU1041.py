import sys
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    count = 0
    for i in range(int(N/4)):
        count += int(sys.stdin.readline())
    print(count)

