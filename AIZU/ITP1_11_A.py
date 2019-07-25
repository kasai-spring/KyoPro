import sys
import copy

dice = [int(x) for x in sys.stdin.readline().split()]  # Top, South, East, West, North, Bottom
order = list(sys.stdin.readline())

for i in order:
    startDice = copy.copy(dice)
    if i == "N":
        dice[0] = startDice[1]
        dice[5] = startDice[4]
        dice[1] = startDice[5]
        dice[4] = startDice[0]
    elif i == "S":
        dice[0] = startDice[4]
        dice[5] = startDice[1]
        dice[1] = startDice[0]
        dice[4] = startDice[5]
    elif i == "E":
        dice[0] = startDice[3]
        dice[5] = startDice[2]
        dice[2] = startDice[0]
        dice[3] = startDice[5]
    elif i == "W":
        dice[0] = startDice[2]
        dice[5] = startDice[3]
        dice[2] = startDice[5]
        dice[3] = startDice[0]

print(dice[0])
