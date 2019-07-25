T,B,U,D,L,R = (int(x) for x in input().split())
box={T:B, B:T, U:D, D:U, L:R, R:L}
nowT = T
nowB = B
N = int(input())
totalCount = 0
for i in range(N):
    p = int(input())
    if nowT == p:
        continue
    if p != nowB:
        nowT = p
        totalCount += 1
    else:
        nowT = p
        totalCount += 2
    #nowB決定
    nowB = box[nowT]
print(totalCount)