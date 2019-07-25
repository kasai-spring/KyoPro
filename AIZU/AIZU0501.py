finish = True
resultPack = []
while finish:
    changeCount = int(input())
    if changeCount == 0:
        finish = True
        break
    changeDict = {}
    for i in range(changeCount):
        inputA = list(input())
        changeDict[str(inputA[0])] = str(inputA[2])
    stringCount = int(input())
    result = ""
    for i in range(stringCount):
        change = list(input())
        changer = str(change[0])
        if changer in changeDict:
            changer = changeDict[changer]
        result += changer
    resultPack.append(result)
for i in resultPack:
    print(i)
