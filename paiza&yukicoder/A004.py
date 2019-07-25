L, n, m = (int(x) for x in input().split())
amidaLottery = [[0 for i in range(n)] for j in range(L)]
# あみだくじ作成
for i in range(m):
    a1, a2, a3 = (int(x) for x in input().split())
    # 右
    amidaLottery[a2][a1 - 1] = "right:" + str(a3)
    # 左
    amidaLottery[a3][a1] = "left:" + str(a2)
# 左下から上に行く
nowX = 0
nowY = L - 1
while True:
    if amidaLottery[nowY][nowX] == 0:
        nowY -= 1
    else:
        direction, number = amidaLottery[nowY][nowX].split(":")
        if direction == "right":
            nowX += 1
            nowY = int(number) - 1
        else:
            nowX -= 1
            nowY = int(number) - 1
    if nowY == 0:
        print(nowX + 1)
        break
