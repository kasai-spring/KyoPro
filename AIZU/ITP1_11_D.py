import copy
import sys

def compare(a, b):
    diceA = a
    diceB = b

    # 上が0の時
    diceX = copy.copy(diceB)
    diceBR = copy.copy(diceB)
    for i in range(4):
        diceBR[3] = diceX[1]
        diceBR[1] = diceX[2]
        diceBR[2] = diceX[4]
        diceBR[4] = diceX[3]
        if diceBR == diceA:
            return False
        diceX = copy.copy(diceBR)

    # 上が5の時
    diceX = [0] * 6
    diceX[0] = diceB[5]
    diceX[5] = diceB[0]
    diceX[1] = diceB[4]
    diceX[2] = diceB[2]
    diceX[3] = diceB[3]
    diceX[4] = diceB[1]
    diceBR = copy.copy(diceX)
    for i in range(4):
        diceBR[1] = diceX[3]
        diceBR[2] = diceX[1]
        diceBR[4] = diceX[2]
        diceBR[3] = diceX[4]
        if diceBR == diceA:
            return False
        diceX = copy.copy(diceBR)

    # 上が1の時
    diceX = [0] * 6
    diceX[0] = diceB[1]
    diceX[5] = diceB[4]
    diceX[1] = diceB[5]
    diceX[2] = diceB[2]
    diceX[3] = diceB[3]
    diceX[4] = diceB[0]
    diceBR = copy.copy(diceX)
    for i in range(4):
        diceBR[3] = diceX[1]
        diceBR[1] = diceX[2]
        diceBR[2] = diceX[4]
        diceBR[4] = diceX[3]
        if diceBR == diceA:
            return False
        diceX = copy.copy(diceBR)

    # 上が4の時
    diceX = [0] * 6
    diceX[0] = diceB[4]
    diceX[5] = diceB[1]
    diceX[1] = diceB[0]
    diceX[2] = diceB[2]
    diceX[3] = diceB[3]
    diceX[4] = diceB[5]
    diceBR = copy.copy(diceX)
    for i in range(4):
        diceBR[3] = diceX[1]
        diceBR[1] = diceX[2]
        diceBR[2] = diceX[4]
        diceBR[4] = diceX[3]
        if diceBR == diceA:
            return False
        diceX = copy.copy(diceBR)

    # 上が2の時
    diceX = [0] * 6
    diceX[0] = diceB[2]
    diceX[5] = diceB[3]
    diceX[1] = diceB[0]
    diceX[2] = diceB[1]
    diceX[4] = diceB[5]
    diceX[3] = diceB[4]
    diceBR = copy.copy(diceX)
    for i in range(4):
        diceBR[3] = diceX[1]
        diceBR[1] = diceX[2]
        diceBR[2] = diceX[4]
        diceBR[4] = diceX[3]
        if diceBR == diceA:
            return False
        diceX = copy.copy(diceBR)

    # 上が3の時
    diceX = [0] * 6
    diceX[0] = diceB[3]
    diceX[5] = diceB[2]
    diceX[1] = diceB[0]
    diceX[2] = diceB[4]
    diceX[4] = diceB[5]
    diceX[3] = diceB[1]
    diceBR = copy.copy(diceX)
    for i in range(4):
        diceBR[3] = diceX[1]
        diceBR[1] = diceX[2]
        diceBR[2] = diceX[4]
        diceBR[4] = diceX[3]
        if diceBR == diceA:
            return False
        diceX = copy.copy(diceBR)

    return True


N = int(sys.stdin.readline())
diceList = [sys.stdin.readline().split() for x in range(N)]
for i in diceList:
    canContinue = True
    for j in diceList:
        status = compare(i, j)
        if status:
            continue
        else:
            if canContinue:
                canContinue = False
            else:
                print("No")
                sys.exit()
else:
    print("Yes")
