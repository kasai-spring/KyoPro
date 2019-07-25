import sys

dice = [int(x) for x in sys.stdin.readline().split()]  # Top, South, East, West, North, Bottom
N = int(sys.stdin.readline())

for i in range(N):
    top, front = (int(x) for x in input().split())
    topLoc = dice.index(top)
    frontLoc = dice.index(front)
    if topLoc == 0:
        if frontLoc == 1:
            print(dice[2])
        elif frontLoc == 4:
            print(dice[3])
        elif frontLoc == 2:
            print(dice[4])
        elif frontLoc == 3:
            print(dice[1])
    elif topLoc == 1:
        if frontLoc == 0:
            print(dice[3])
        elif frontLoc == 5:
            print(dice[2])
        elif frontLoc == 2:
            print(dice[0])
        elif frontLoc == 3:
            print(dice[5])
    elif topLoc == 2:
        if frontLoc == 0:
            print(dice[1])
        elif frontLoc == 5:
            print(dice[4])
        elif frontLoc == 1:
            print(dice[5])
        elif frontLoc == 4:
            print(dice[0])
    elif topLoc == 3:
        if frontLoc == 0:
            print(dice[4])
        elif frontLoc == 5:
            print(dice[1])
        elif frontLoc == 1:
            print(dice[0])
        elif frontLoc == 4:
            print(dice[5])
    elif topLoc == 4:
        if frontLoc == 0:
            print(dice[2])
        elif frontLoc == 5:
            print(dice[3])
        elif frontLoc == 2:
            print(dice[5])
        elif frontLoc == 3:
            print(dice[0])
    elif topLoc == 5:
        if frontLoc == 1:
            print(dice[3])
        elif frontLoc == 4:
            print(dice[2])
        elif frontLoc == 2:
            print(dice[1])
        elif frontLoc == 3:
            print(dice[4])
