import copy


def rotate(r, m, tgp):  # rは回転数、mはピースの辺、tgpは回転するピースの配列
    startpiece = copy.deepcopy(tgp)
    endpiece = copy.deepcopy(tgp)
    for i in range(r):
        for j in range(m):
            for k in range(m):
                endpiece[j][k] = startpiece[m - 1 - k][j]
        else:
            startpiece = copy.deepcopy(endpiece)

    return endpiece


X, N, M = (int(x) for x in input().split())

puzzle = [[1 if i == "Y" else 0 for i in list(input())] for j in range(N)]
piece = [[[1 if i == "Y" else 0 for i in list(input())] for j in range(M)] for k in range(X)]
disAPuzzle = []
disAPuzzleIndex = []
pieceCanArea = int(N / M)
# パズルを分解
for i in range(pieceCanArea):
    for j in range(pieceCanArea):
        count = 0
        onePiece = []
        for k in range(M):
            onePieceSide = []
            for l in range(M):
                onePieceSide.append(puzzle[i * M + k][j * M + l])
            onePiece.append(onePieceSide)
        disAPuzzle.append(onePiece)
        disAPuzzleIndex.append(str(i * M + 1) + " " + str(j * M + 1))

for i in range(len(piece)):  # ピースごとに検証
    pieceTotal = sum(map(sum, piece[i]))
    # パズルのピースがはまる場所ごとに検証
    for j in range(len(disAPuzzle)):
        puzzleTotal = sum(map(sum, disAPuzzle[j]))
        if puzzleTotal != pieceTotal:  # ピースの数が合わないものは次にスキップ
            continue
        if piece[i] == disAPuzzle[j]:
            print(disAPuzzleIndex[j] + " 0")
            break
        rotatePiece = rotate(1, M, piece[i])
        # 1回転
        if rotatePiece == disAPuzzle[j]:
            print(disAPuzzleIndex[j] + " 1")
            break
        # 2回転
        rotatePiece = rotate(2, M, piece[i])
        if rotatePiece == disAPuzzle[j]:
            print(disAPuzzleIndex[j] + " 2")
            break
        # 3回転
        rotatePiece = rotate(3, M, piece[i])
        if rotatePiece == disAPuzzle[j]:
            print(disAPuzzleIndex[j] + " 3")
            break

    else:
        print(-1)
