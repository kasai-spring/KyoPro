finish = list("END OF INPUT")
while True:
    inputList = list(input())
    if inputList == finish:
        break
    count = 0
    printList = []
    isBeforeSpace = False
    for i in inputList:
        if i == " ":
            if isBeforeSpace:
                printList.append(0)
            else:
                printList.append(count)
                count = 0
                isBeforeSpace = True
        else:
            isBeforeSpace = False
            count += 1
    else:
        if count > 0:
            printList.append(count)
    print("".join(map(str, printList)))
