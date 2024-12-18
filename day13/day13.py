

import sys
from collections import defaultdict,Counter
from functools import cache
sys.stdin = open('./day13/input.txt', 'r')
sys.stdout = open('./day13/output.txt', 'w')
sys.setrecursionlimit(10**6)

def aoc13_1():
    tot = 0
    a = []
    b = []
    x,y = 0,0
    def opt():
        t1,t2 = (x * b[1] - y * b[0]) ,(a[0] * b[1] - a[1] * b[0])
        if t1 % t2 != 0:
            return 0
        r1 = t1 // t2
        if (x - r1 * a[0] ) % b[0]  != 0:
            return 0
        r2 = (x - r1 * a[0] ) // b[0]
        return r1* 3 + r2
    try:
        while True:
            a.clear()
            b.clear()
            s = input().split(':')[-1].split(',')
            a.append(int(s[0].split('+')[-1]))
            a.append(int(s[1].split('+')[-1]))
            s = input().split(':')[-1].split(',')
            b.append(int(s[0].split('+')[-1]))
            b.append(int(s[1].split('+')[-1]))
            s = input().split(':')[-1].split(',')
            x = int(s[0].split('=')[-1])
            y = int(s[1].split('=')[-1])
            tot += opt()
            input()
    except EOFError:
        pass
    print(tot)


def aoc13_2():
    tot = 0
    a = []
    b = []
    x,y = 0,0
    def opt():
        t1,t2 = (x * b[1] - y * b[0]) ,(a[0] * b[1] - a[1] * b[0])
        if t1 % t2 != 0:
            return 0
        r1 = t1 // t2
        if (x - r1 * a[0] ) % b[0]  != 0:
            return 0
        r2 = (x - r1 * a[0] ) // b[0]
        return r1* 3 + r2
    try:
        while True:
            a.clear()
            b.clear()
            s = input().split(':')[-1].split(',')
            a.append(int(s[0].split('+')[-1]))
            a.append(int(s[1].split('+')[-1]))
            s = input().split(':')[-1].split(',')
            b.append(int(s[0].split('+')[-1]))
            b.append(int(s[1].split('+')[-1]))
            s = input().split(':')[-1].split(',')
            x = int(s[0].split('=')[-1]) + 10000000000000
            y = int(s[1].split('=')[-1]) + 10000000000000
            tot += opt()
            input()
    except EOFError:
        pass
    print(tot)

aoc13_2()


