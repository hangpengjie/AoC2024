

import sys
from collections import defaultdict,Counter
sys.stdin = open('./day5/input.txt', 'r')
sys.stdout = open('./day5/output.txt', 'w')

def aoc5_1():
    tot = 0
    g = [set() for i in range(100)]
    def opt(z:list):
        t = set()
        t.add(z[0])
        for i in range(1,len(z)):
            if not g[z[i]].issuperset(t):
                return 0
            t.add(z[i])
        return z[len(z) // 2]

    try:
        while True:
            s = input()
            if len(s) == 0:
                break
            u,v = map(int,s.split('|'))
            g[v].add(u)
            
        while True:
            z = list(map(int,input().split(',')))
            tot += opt(z)

    except EOFError:
        pass
    print(tot)

def aoc5_2():
    tot = 0
    g = [set([i]) for i in range(100)]
    def opt0(z:list):
        t = set()
        t.add(z[0])
        for i in range(1,len(z)):
            if not g[z[i]].issuperset(t):
                return 0
            t.add(z[i])
        return z[len(z) // 2]
    def opt(z:list):
        t = set()
        for x in z:
            t.add(x)
        p = []
        while len(t) > 0:
            for x in t:
                if g[x].issuperset(t):
                    p.append(x)
                    t.remove(x)
                    break
                    
                    
        return p[len(p) // 2]

    try:
        while True:
            s = input()
            if len(s) == 0:
                break
            u,v = map(int,s.split('|'))
            g[v].add(u)
            
        while True:
            z = list(map(int,input().split(',')))
            tot += opt(z) - opt0(z)

    except EOFError:
        pass
    print(tot)

aoc5_2()