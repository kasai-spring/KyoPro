y,m,d= map(int,input().split(" "))
G=["明治","大正","昭和","平成","令和"]
if (y<1912) or (y==1912 and m<7) or (y==1912 and m==7 and d<=29):
    print(G[0]+str(y-1867)+"年"+str(m)+"月"+str(d)+"日")


elif (1912 < y < 1926) or (y==1912 and m>7) or (y==1912 and m==7 and d==30) or (y==1926 and m<12) or (y==1926 and m==12 and d<=24):
    if y==1912:
        print(G[1]+"元年"+str(m)+"月"+str(d)+"日")
    else:
        print(G[1]+str(y-1911)+"年"+str(m)+"月"+str(d)+"日")


elif (1926 < y <1989) or (y==1926 and m==12 and d>=25) or (y==1989 and m==1 and d<=7):
    if y==1926:
        print(G[2]+"元年"+str(m)+"月"+str(d)+"日")
    else:
        print(G[2]+str(y-1925)+"年"+str(m)+"月"+str(d)+"日")


elif (1989 < y < 2019)or(y==1989 and m>2)or(y==1989 and m==1 and d>=8)or(y==2019 and m<5):
    if y==1989:
        print(G[3]+"元年"+str(m)+"月"+str(d)+"日")
    else:
        print(G[3]+str(y-1988)+"年"+str(m)+"月"+str(d)+"日")


else:
    if y==2019:
        print(G[4]+"元年"+str(m)+"月"+str(d)+"日")
    else:
        print(G[4]+str(y-2018)+"年"+str(m)+"月"+str(d)+"日")