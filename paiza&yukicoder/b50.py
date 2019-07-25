N = int(input())
S = list(input())
for i in range(N):
    status = 0
    t = list(input())
    for j in range(len(t)):
        count = 0
        invalid = 0
        if status==1:
            break
        if t[j]==S[0]:
            z = j-1
            for k in range(len(S)):
                if z+1<len(t):
                    z+=1
                else:
                    break
                if t[z]==S[k]:
                    count+=1
                else:
                    for l in range(k,len(S)):
                        if z+1<len(t):
                            z+=1
                        else:
                            invalid=1
                            break
                        if t[z]==S[l]:
                            count += 1
                        else:
                            invalid = 1
                            break
                        if count == len(S):
                            status=1
                            print("valid")
                            break
                if status == 1:
                    break

                if count==len(S):
                    status = 1
                    print("valid")
                    break

                if invalid==1:
                    break
        else:
            continue
    if status ==0:
        print("invalid")
