input = int(input())
if input % 4 == 0:
    if input % 100==0:
        if input % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
else:
    print("No")