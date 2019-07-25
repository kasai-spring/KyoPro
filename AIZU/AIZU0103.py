N = int(input())
for i in range(N):
    finish = True
    point = 0
    Out = 0
    base = [0,0,0]
    while finish:
        status = input()
        if status =="HIT":
            if base[2]==1:
                point+=1
                base[2]=0
            if base[1]==1:
                base[2]=1
                base[1]=0
            if base[0]==1:
                base[1]=1
                base[0]=0
            base[0]=1
        elif status=="HOMERUN":
            point += base.count(1)
            point += 1
            base[0]=0
            base[1]=0
            base[2]=0
        elif status =="OUT":
            Out += 1
        
        if Out ==3:
            print(point)
            finish = False
