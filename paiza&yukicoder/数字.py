N = int(input())
minN = 0
maxN = 101
perN = []
for i in range(N):
    inputA = input()
    inputB=inputA.split()
    y=inputB[0]
    m=int(inputB[1])
    if(y==">"):
        if minN<m:
            minN = m
    if(y=="<"):
        if maxN>m:
            maxN = m
    if(y=="/"):
        perN.append(m)
fin = 0
i = 1
print(minN,maxN,perN)
while fin<1:
    if maxN==101:
        if len(perN)!=0:
            count=0
            for j in perN:
                if minN<i and i%j==0:
                    count+=1
            if len(perN)==count:
                print(i)
                fin += 1
                break
        else:
            if minN<i:
                print(i)
                fin += 1
                break
        
    else:
        if len(perN)!=0:
            count=0
            for j in perN:
                if minN<i<maxN and i%j==0:
                    count+=1
            if len(perN)==count:
                print(i)
                fin += 1
                break
        else:
            if minN<i<maxN:
                print(i)
                fin+=1
                break
    i+=1

