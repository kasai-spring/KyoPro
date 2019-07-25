import copy
dice = [1, 6, 2, 5, 4, 3]  # Top,Bottom,North South,East,West
N, H, W = (int(x) for x in input().split())
flag = [[0 for i in range(W)] for j in range(H)]
nowH, nowW = (int(x) for x in input().split())
nowW -= 1
nowH -= 1
flag[nowH][nowW] = 6
root = list(input())
for i in range(N):
    startDice = copy.copy(dice)  # 参照用
    # 転がす
    if root[i] == "U":
        nowH -= 1
        dice[0] = startDice[3]
        dice[1] = startDice[2]
        dice[2] = startDice[0]
        dice[3] = startDice[1]
    elif root[i] == "D":
        nowH += 1
        dice[0] = startDice[2]
        dice[1] = startDice[3]
        dice[2] = startDice[1]
        dice[3] = startDice[0]
    elif root[i] == "R":
        nowW += 1
        dice[0] = startDice[5]
        dice[1] = startDice[4]
        dice[4] = startDice[0]
        dice[5] = startDice[1]
    elif root[i] == "L":
        nowW -= 1
        dice[0] = startDice[4]
        dice[1] = startDice[5]
        dice[4] = startDice[1]
        dice[5] = startDice[0]
    # 色塗る
    flag[nowH][nowW] = dice[1]

for i in flag:
    print(" ".join(map(str, i)))
