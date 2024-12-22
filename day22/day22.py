import sys
from collections import defaultdict, Counter,deque
from queue import PriorityQueue
from functools import cache
from itertools import permutations
sys.stdin = open('./day22/input.txt', 'r')
sys.stdout = open('./day22/output.txt', 'w')
sys.setrecursionlimit(10**5)



def aoc22_1():
    g = []
    try:
        while True:
            g.append(int(input()))
    except EOFError:
        pass
    mod = 16777216
    def opt1(x):
        return (x ^ (x << 6)) % mod
    
    def opt2(x):
        return (x ^ (x >> 5)) % mod
    
    def opt3(x):
        return (x ^ (x << 11)) % mod

    def opt(x):
        return opt3(opt2(opt1(x)))
    tot = 0
    for x in g:
        for _ in range(2000):
            x = opt(x)
            print(x)
        tot += x
    print(tot)

def aoc22_2():
    g = []
    try:
        while True:
            g.append(int(input()))
    except EOFError:
        pass
    mod = 16777216
    def hash(a,b,c,d):
        a,b,c,d = a + 9, b + 9, c + 9, d + 9
        return a * 10 ** 6 + b * 10 ** 4 + c * 10 ** 2 + d 
    def opt1(x):
        return (x ^ (x << 6)) % mod
    
    def opt2(x):
        return (x ^ (x >> 5)) % mod
    
    def opt3(x):
        return (x ^ (x << 11)) % mod
    def opt(x):
        return opt3(opt2(opt1(x)))
    
    mp = defaultdict(list)

    for idx,x in enumerate(g):
        p = [-1,-1,-1]
        pre = x % 10
        for i in range(2000):
            x = opt(x)
            m = x % 10 
            if i < 3:
                p[i] = m - pre
            else:
                h = hash(p[0],p[1],p[2],m - pre)
                p[0],p[1],p[2] = p[1],p[2],m - pre
                z = mp[h]
                if not z:
                    z.append(m)
                    z.append(idx)
                else:
                    if z[1] != idx:
                        z[0] += m
                        z[1] = idx
            pre = m
    mx = 0
    for k,v in mp.items():
        mx = max(mx,v[0])
    print(mx)   
    
aoc22_2()