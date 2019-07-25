book = {}

try:
    while True:
        w, n = input().split()
        if w in book:
            book[w].append(int(n))
        else:
            book[w] = [int(n)]
except EOFError:
    pass

book_sort = sorted(book)
book_sort.sort()
for i in book_sort:
    printList = list(set(book[i]))
    printList.sort()
    print(i)
    print(" ".join(map(str, printList)))
    # 数字だとjoin時にエラー 文字列だとsortがうまくできない
