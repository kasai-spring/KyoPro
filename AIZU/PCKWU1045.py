import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    a_list = [int(x) for x in sys.stdin.readline().split()]
    s = sum(a_list)
    a_list = [a * 2 for a in a_list]
    _list = [-s]
    for i in a_list:
        _list.extend([j + i for j in _list])
    print(min(map(abs, _list)))
