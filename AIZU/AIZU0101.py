N = int(input())
for i in range(N):
    stri = list(input())
    for i in range(len(stri)):
        try:
            if stri[i]=="H" and stri[i+1]=="o" and stri[i+2] =="s" and stri[i+3] =="h" and stri[i+4] =="i" and stri[i+5] =="n" and stri[i+6] =="o":
                stri[i+6] ="a"
        except IndexError:
            break
    print("".join(stri))