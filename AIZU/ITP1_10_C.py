import sys
from statistics import pstdev

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    number = [int(i) for i in sys.stdin.readline().split()]
    pst = pstdev(number)
    print(pst)
