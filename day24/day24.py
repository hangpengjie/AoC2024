import sys
from collections import defaultdict, Counter,deque
from queue import PriorityQueue
from functools import cache
from itertools import permutations
sys.stdin = open('./day24/input.txt', 'r')
sys.stdout = open('./day24/output.txt', 'w')
sys.setrecursionlimit(10**5)

def aoc24_1():
    reg = {}
    z = defaultdict(list)
    try:
        while True:
            s = input()
            if s:
                k,v = s.split(': ')
                reg[k] = int(v)
            else:
                break
        while True:
            s = input().split(' -> ')
            k = s[0].split(' ')
            z[(k[0],k[1], k[2])].append(s[1])
    except EOFError:
        pass
    def opt(a,op,b, v):
        res = 0
        if op == 'AND':
            res = a&b
        elif op == 'OR':
            res = a|b
        else:
            res = a^b
        reg[v] = res
    while z:
        q = []
        for k,v in z.items():
            a,op,b = k
            if a in reg and b in reg:
                for t in v:
                    opt(reg[a],op,reg[b],t)
                q.append(k)
        for k in q:
            del z[k]
    res = []
    for k,v in reg.items():
        if k.startswith('z') and k[1:].isdigit():
            res.append((int(k[1:]),v))
    res.sort()
    ans = 0
    while res:
        ans = ans*2 + res.pop()[1]
    print(ans)

aoc24_1()
        
            

