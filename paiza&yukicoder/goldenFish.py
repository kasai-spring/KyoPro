fishlist = []
M,N,x = (int(x) for x in input().split())
for i in range(M):
    fishlist.append(int(input()))
getFish = 0
for i in range(N):
    pHp = x
    while pHp>0:
        pHp -= fishlist[0]
        if pHp>0:
            getFish += 1
            del fishlist[0]
print(getFish)
    

