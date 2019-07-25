finish = True
while finish:
    H, W = (int(x) for x in input().split())
    if H == 0 and W == 0:
        finish = False
        break
    room = [list(input()) for i in range(H)]
    remainL = []
    roomM = True
    nowH = 0
    nowW = 0
    while roomM:
        if room[nowH][nowW] == ">":
            nowW += 1
        elif room[nowH][nowW] == "<":
            nowW -= 1
        elif room[nowH][nowW] == "^":
            nowH -= 1
        elif room[nowH][nowW] == "v":
            nowH += 1
        else:
            print(str(nowW) + " " + str(nowH))
            roomM = False
            break
        nowList = str(nowH) + str(nowW)
        if nowList in remainL:
            print("LOOP")
            roomM = False
        remainL.append(str(nowH) + str(nowW))
