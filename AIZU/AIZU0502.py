import copy

printResult = []
while True:
    N = int(input())
    if N == 0: a
    break
totalCount = 1
dice = [1, 6, 5, 2, 3, 4]  # Top,Bottom,North South,East,West
for i in range(N):
    startDice = copy.copy(dice)
    direction = input()
    if direction == "North":
        dice[0] = startDice[3]
        dice[1] = startDice[2]
        dice[2] = startDice[0]
        dice[3] = startDice[1]
    elif direction == "South":
        dice[0] = startDice[2]
        dice[1] = startDice[3]
        dice[2] = startDice[1]
        dice[3] = startDice[0]

    elif direction == "East":
        dice[0] = startDice[5]
        dice[1] = startDice[4]
        dice[4] = startDice[0]
        dice[5] = startDice[1]

    elif direction == "West":
        dice[0] = startDice[4]
        dice[1] = startDice[5]
        dice[4] = startDice[1]
        dice[5] = startDice[0]

    elif direction == "Right":
        dice[2] = startDice[5]
        dice[3] = startDice[4]
        dice[4] = startDice[2]
        dice[5] = startDice[3]

    else:
        dice[2] = startDice[4]
        dice[3] = startDice[5]
        dice[4] = startDice[3]
        dice[5] = startDice[2]

    totalCount += dice[0]
printResult.append(totalCount)

for i in printResult:
    print(i)
