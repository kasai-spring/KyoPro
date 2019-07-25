import copy
N = int(input())
count = 0
bookcase = [int(e) for e in input().split()]
for i in range(len(bookcase)):
    if i==0:
        minN = min(bookcase)
        if bookcase[i]!=minN:
            index=bookcase.index(minN)
            before = bookcase[0]
            after = bookcase[index]
            bookcase[0]=after
            bookcase[index]=before
            count+=1
    else:
        tempcase = bookcase.copy()
        del tempcase[:i]
        minN = min(tempcase)
        if bookcase[i]>minN:
            index=bookcase.index(minN)
            before = bookcase[i]
            after = bookcase[index]
            bookcase[i]=after
            bookcase[index]=before
            count+=1
print(count)
