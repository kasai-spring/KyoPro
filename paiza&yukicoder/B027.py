H, W, N = (int(x) for x in input().split())
card = [list(input().split()) for x in range(H)]
n_List = [0] * N
gameCount = int(input())
playerNumber = 0
for i in range(gameCount):
    aX, aY, bX, bY = (int(x) for x in input().split())
    if card[aX - 1][aY - 1] == card[bX - 1][bY - 1]:
        n_List[playerNumber] += 2
    else:
        playerNumber += 1
        if playerNumber >= N:
            playerNumber = 0

for i in n_List:
    print(i)
