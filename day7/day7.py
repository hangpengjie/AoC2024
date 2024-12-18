

import sys
from collections import defaultdict,Counter
sys.stdin = open('./day7/input.txt', 'r')
sys.stdout = open('./day7/output.txt', 'w')
sys.setrecursionlimit(10**6)

def aoc7_1():
    tot = 0
    r = 0
    t = []
    def opt(idx,cur):
        nonlocal tot
        if idx == len(t):
            if cur == r:
                return True
            else:
                return False
        return opt(idx+1,cur + t[idx]) or opt(idx+1,cur * t[idx])
    try:
        while True:
            s = input().split(':')
            r = int(s[0])
            t = list(map(int,s[1].split()))
            if opt(1, t[0]):
                tot += r
            
    except EOFError:
        pass
    print(tot)


def aoc7_2():
    tot = 0
    r = 0
    t = []
    def opt(idx,cur):
        nonlocal tot
        if idx == len(t):
            if cur == r:
                return True
            else:
                return False
        return opt(idx+1,cur + t[idx]) or opt(idx+1,cur * t[idx]) or opt(idx+1,int(str(cur) + str(t[idx]))) 
    try:
        while True:
            s = input().split(':')
            r = int(s[0])
            t = list(map(int,s[1].split()))
            if opt(1, t[0]):
                tot += r
            
    except EOFError:
        pass
    print(tot)
aoc7_2()