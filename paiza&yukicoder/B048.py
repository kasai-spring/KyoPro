import sys
import copy


def check(templist, size):
    # 横
    result = 0
    for y in range(size):
        for x in range(size):
            if templist[y][x] == 0:
                continue
            else:
                break
        else:
            result += 1
    # 縦
    for x in range(size):
        for y in range(size):
            if templist[y][x] == 0:
                continue
            else:
                break
        else:
            result += 1
    # 斜め
    for x in range(size):
        if templist[x][x] == 0:
            continue
        else:
            break
    else:
        result += 1

    for x in range(size):
        if templist[x][size - 1 - x] == 0:
            continue
        else:
            break
    else:
        result += 1

    return result


N, M = (int(x) for x in sys.stdin.readline().split())
bingo = [[int(x) for x in sys.stdin.readline().split()] for i in range(N)]
for i in range(M):
    try:
        callNumber = int(sys.stdin.readline())
    except:
        pass

    for j in range(N):  # TODO 完全にリスト内包表記に変更
        bingo[j] = [0 if x == callNumber else int(x) for x in bingo[j]]
maxBingo = 0
for i in range(N):
    for j in range(N):
        if bingo[i][j] == 0:
            continue
        tempBingo = copy.deepcopy(bingo)
        tempBingo[i][j] = 0
        bingoCount = check(tempBingo, N)
        if maxBingo < bingoCount:
            maxBingo = bingoCount
print(maxBingo)
