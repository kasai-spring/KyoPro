ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
S = input()
s_List = list(S)
finish = True
while finish:
    startBracketsNumber = -1
    endBracketsNumber = -1
    # 一番小さい子の括弧を抽出
    for i in range(len(s_List)):
        if s_List[i] == "(":
            startBracketsNumber = i
        if s_List[i] == ")":
            endBracketsNumber = i
            break
    else:  # 括弧が存在しない場合
        finish = True
        break
    # 抽出した括弧の外側の数字判定
    isBeforeNumber = False
    beforeNumber = str(1)
    testCount = 0
    for i in reversed(range(0, startBracketsNumber)):
        rS = str(s_List[i])
        if rS.isdigit():
            if isBeforeNumber:
                beforeNumber += rS
            else:
                beforeNumber = rS
                isBeforeNumber = True
        else:
            break
    beforeNumber = beforeNumber[::-1]
    # 抽出した括弧の内部を処理
    extractionList = [0]*26
    extractNumber = str(1)
    isExtBeforeNumber = False
    for i in s_List[startBracketsNumber+1:endBracketsNumber]:
        if str(i).isdigit():
            tempIex = str(i)
            if isExtBeforeNumber:
                extractNumber += tempIex
            else:
                extractNumber = tempIex
                isExtBeforeNumber = True
        else:
            extractionList[ALPHABET.index(i)] += int(extractNumber)
            extractNumber = str(1)
            isExtBeforeNumber = False
    # 計算した内部の数をリスト化
    insertList = []
    for i in range(len(extractionList)):
        if extractionList[i] == 0:
            pass
        else:
            tempResult = extractionList[i] * int(beforeNumber)
            tempList = list(str(tempResult))
            for j in tempList:
                insertList.append(j)
            insertList.append(ALPHABET[i])
    # 最初に抽出した括弧を削除しリスト化したものを挿入
    startDel = startBracketsNumber-len(str(beforeNumber))
    del s_List[startDel:endBracketsNumber+1]
    for i in range(len(insertList)):
        s_List.insert(startDel+i, insertList[i])
alpCount = [0]*26
tempCount = str(1)
isResultNumber = False
for i in s_List:
    if str(i).isdigit():
        if isResultNumber:
            tempCount += str(i)
        else:
            tempCount = str(i)
            isResultNumber = True
    else:
        alpCount[ALPHABET.index(i)] += int(tempCount)
        tempCount = str(1)
        isResultNumber = False

for i in range(26):
    print(str(ALPHABET[i])+" "+str(alpCount[i]))
