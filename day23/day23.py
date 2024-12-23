import sys
from collections import defaultdict, Counter,deque
from queue import PriorityQueue
from functools import cache
from itertools import permutations
sys.stdin = open('./day23/input.txt', 'r')
sys.stdout = open('./day23/output.txt', 'w')
sys.setrecursionlimit(10**5)

def aoc23_1() :
    mp = defaultdict(set)
    try:
        while True:
            s = input().split('-')
            mp[s[0]].add(s[1])
            mp[s[1]].add(s[0])
    except EOFError:
        pass
    tot = 0
    for a,v in mp.items():
        for b in v:
            for c,w in mp.items():
                if b in w and a in w:
                    if a.startswith('t') or b.startswith('t') or c.startswith('t'):
                        tot += 1
    print(tot//6)


def aoc23_2():
    mp = defaultdict(set)
    try:
        while True:
            s = input().split('-')
            mp[s[0]].add(s[1])
            mp[s[1]].add(s[0])
    except EOFError:
        pass
    mx,ans = 0, []
    def opt(cur:str,vis:set):
        nonlocal mx,ans
        vis = list(vis)
        #vis.add(cur)
        n = len(vis)
        for i in range(1 << n):
            s = [cur]
            for j in range(n):
                if i & (1 << j):
                    s.append(vis[j])
            if len(s) <= mx:
                continue
            for x in s:
                for y in s:
                    if x != y and y not in mp[x]:
                        break
                else:
                    continue
                break
            else:
                mx = len(s)
                ans = s
    for a,v in mp.items():
        opt(a,v)
    print(','.join(sorted(ans)))

aoc23_2()