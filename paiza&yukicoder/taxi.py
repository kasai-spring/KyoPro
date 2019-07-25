N,X = map(int,input().split())
minP = 0
maxP = 0
for i in range(N):
    a,b,c,d = map(int,input().split())
    if a>X:
        if i==0:
            minP = b
            maxP = b
        else:
            if minP>b:
                minP=b
            if maxP<b:
                maxP=b
    else:
        count = 0
        count = ((X-a)//c)
        count +=1
        price = b+d*count
        if i==0:
            minP = price
            maxP = price
        else:
            if minP>price:
                minP = price
            if maxP<price:
                maxP = price
                
print(minP,maxP)