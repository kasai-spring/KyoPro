# gcd関数はpython3.4だとfractionsモジュールにある。3.5以上だとmathモジュール

import sys
import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


n = int(sys.stdin.readline())
t = [int(x) for x in sys.stdin.readlines()]
total_lcm = 1
for i in t:
    total_lcm = lcm(total_lcm, i)
print(total_lcm)
