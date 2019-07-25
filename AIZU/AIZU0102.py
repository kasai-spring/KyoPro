import copy
finish = True
while finish:
    N = int(input())
    if N==0:
        finish = False
        break
    box = [[int(i) for i in input().split()] for j in range(N)]
    resultBox = copy.copy(box)
    #横
    for i in range(N):
        result = 0
        for j in range(N):
            result += box[i][j]
        resultBox[i].append(result)
    #縦
    for i in range(N):
        result = 0
        for j in range(N):
            result += box[j][i]
        try:
            resultBox[N].append(result)
        except IndexError:
            resultBox.append([])
            resultBox[N].append(result)
        
    #右下
    #縦
    allR = 0
    for i in range(N):
        allR += resultBox[i][N]
    resultBox[N].append(allR)

    for i in range(N+1):
        for j in range(N+1):
            for k in range(5-len(str(resultBox[i][j]))):
                print(" ",end="")
            print(resultBox[i][j],end="")
        print()
