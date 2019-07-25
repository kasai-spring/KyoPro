import sys
import copy


def is_stable(before, after):
    before_dic = {}
    for ii in before:
        if list(ii)[1] in before_dic:
            before_dic[list(ii)[1]] += list(ii)[0]
        else:
            before_dic[list(ii)[1]] = list(ii)[0]
    after_dic = {}
    for ii in after:
        if list(ii)[1] in after_dic:
            after_dic[list(ii)[1]] += list(ii)[0]
        else:
            after_dic[list(ii)[1]] = list(ii)[0]
    for ii in before_dic:
        if before_dic[ii] == after_dic[ii]:
            continue
        else:
            return False
    return True


N = int(sys.stdin.readline())
card = sys.stdin.readline().split()
# BubbleSort
bubbleCard = copy.copy(card)
while True:
    changeStatus = True
    for i in reversed(range(N)):
        if i == 0:
            break
        if int(list(bubbleCard[i])[1]) < int(list(bubbleCard[i - 1])[1]):
            bubbleCard[i], bubbleCard[i - 1] = bubbleCard[i - 1], bubbleCard[i]
            changeStatus = False
    if changeStatus:
        break

print(" ".join(bubbleCard))
if is_stable(card, bubbleCard):
    print("Stable")
else:
    print("Not stable")
# SelectSort
selectCard = copy.copy(card)
for i in range(N):
    minJ = i
    for j in range(i, N):
        if int(list(selectCard[j])[1]) < int(list(selectCard[minJ])[1]):
            minJ = j
    selectCard[i], selectCard[minJ] = selectCard[minJ], selectCard[i]
print(" ".join(selectCard))
if is_stable(card, selectCard):
    print("Stable")
else:
    print("Not stable")
