H,W = (int(x) for x in input().split())
resultP = [[0 for i in range(W)] for j in range(H)]
a_1,b_1 = (int(x) for x in input().split())
a_2,b_2 = (int(x) for x in input().split())
resultP[0][0] = a_1
resultP[0][1] = b_1
resultP[1][0] = a_2
resultP[1][1] = b_2


for i in range(2):
    change = resultP[i][1]-resultP[i][0]
    for j in range(2,W):
        resultP[i][j]=resultP[i][j-1]+change

for i in range(W):
    change = resultP[1][i]-resultP[0][i]
    for j in range(2,H):
        resultP[j][i]=resultP[j-1][i]+change
first = True
for i in resultP:
    for j in i:
        if first:
            print(str(j),end="")
            first = False
        else:
            print(" "+str(j), end="")
    print()
    first = True

        



