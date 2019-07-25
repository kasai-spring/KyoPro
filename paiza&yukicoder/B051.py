N = int(input())
magicSquare = [[int(x) for x in input().split()] for i in range(N)]
# まず合計数を求める
totalNumber = 0
for i in range(N):
    finish = False
    for j in range(N):
        if magicSquare[i][j] == 0:
            totalNumber = 0
            break
        else:
            totalNumber += magicSquare[i][j]
    else:
        finish = True
    if finish:
        break
# 横
for i in range(N):
    isSecondZero = False
    zeroPoint = [-1, -1]
    sideResult = 0
    for j in range(N):
        if magicSquare[i][j] == 0:
            if isSecondZero:
                break
            else:
                zeroPoint = [i, j]
                isSecondZero = True
        else:
            sideResult += magicSquare[i][j]
    else:
        if isSecondZero:
            magicSquare[zeroPoint[0]][zeroPoint[1]] = totalNumber - sideResult
            # ゼロポイントに代入してあったもので位置を指定し、合計数から横の合計を引いたものを代入
        else:
            pass
# 縦
for i in range(N):
    isSecondZero = False
    zeroPoint = [-1, -1]
    sideResult = 0
    for j in range(N):
        if magicSquare[j][i] == 0:
            if isSecondZero:
                break
            else:
                zeroPoint = [j, i]
                isSecondZero = True
        else:
            sideResult += magicSquare[j][i]
    else:
        if isSecondZero:
            magicSquare[zeroPoint[0]][zeroPoint[1]] = totalNumber - sideResult
            # ゼロポイントに代入してあったもので位置を指定し、合計数から横の合計を引いたものを代入
        else:
            pass

for i in magicSquare:
    print(" ".join(map(str, i)))
