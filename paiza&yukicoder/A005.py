a, b, n = (int(x) for x in input().split())
frame = [0]*a
throwInput = input().split()
before = -1
frameCount = 0
isSecond = False
# Gを0に変換&int型に変換
throwList = [0 if i == "G" else int(i) for i in throwInput]
for i in range(len(throwList)):
    # 二投目か判断
    if before == -1:
        before = throwList[i]
        isSecond = False
    else:
        before += throwList[i]
        frame[frameCount] = before
        isSecond = True
    # スペアとストライク処理
    if before == b:
        if isSecond:  # スペア
            try:
                before += throwList[i+1]
            except IndexError:
                pass
            if frameCount == a-1 and i < n-1:
                continue
            frame[frameCount] = before
            frameCount += 1
            before = -1

        else:  # ストライク
            try:
                before += throwList[i+1]
                before += throwList[i + 2]
            except IndexError:
                pass
            if frameCount == a-1 and i < n-1:
                continue
            frame[frameCount] = before
            frameCount += 1
            before = -1
    else:
        if isSecond:  # 二回投げたので代入
            if frameCount == a-1 and i < n-1:
                continue
            frame[frameCount] = before
            frameCount += 1
            before = -1
        else:
            continue
print(sum(frame))
