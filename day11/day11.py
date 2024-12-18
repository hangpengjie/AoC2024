

import sys
from collections import defaultdict,Counter
from functools import cache
sys.stdin = open('./day11/input.txt', 'r')
sys.stdout = open('./day11/output.txt', 'w')
sys.setrecursionlimit(10**6)

def aoc11_1():
    tot = 0
    g = list(map(int, input().split()))

    def opt(x, cnt):
        if cnt == 0:
            return 1
        if x == 0:
            return opt(1, cnt - 1)
        t = str(x)
        if len(t) % 2 == 0:
            return opt(int(t[:len(t) // 2]), cnt - 1) + opt(int(t[len(t) // 2:]), cnt - 1)
        return opt(x * 2024, cnt - 1)
    for x in g:
        tot += opt(x, 25)
    print(tot)

def aoc11_2():
    tot = 0
    g = list(map(int, input().split()))

    @cache
    def opt(x, cnt):
        if cnt == 0:
            return 1
        if x == 0:
            return opt(1, cnt - 1)
        t = str(x)
        if len(t) % 2 == 0:
            return opt(int(t[:len(t) // 2]), cnt - 1) + opt(int(t[len(t) // 2:]), cnt - 1)
        return opt(x * 2024, cnt - 1)
    for x in g:
        tot += opt(x, 75)
    print(tot)

aoc11_2()