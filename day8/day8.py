

import sys
from collections import defaultdict,Counter
sys.stdin = open('./day8/input.txt', 'r')
sys.stdout = open('./day8/output.txt', 'w')
sys.setrecursionlimit(10**6)

def aoc8_1():
    tot = 0
    d = defaultdict(list)
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    n,m = len(g),len(g[0])
    for i in range(n):
        for j in range(m):
            if g[i][j] != '.':
                d[g[i][j]].append((i,j))
    diff = set()
    for _,v in d.items():
        for i in range(len(v)):
            for j in range(i+1,len(v)):
                dx = v[j][0] - v[i][0]
                dy = v[j][1] - v[i][1]
                nx,ny = v[j][0] + dx,v[j][1] + dy
                if nx < n and ny < m and nx >= 0 and ny >= 0:
                    diff.add((nx,ny))
                nx, ny = v[i][0] - dx, v[i][1] - dy
                if nx < n and ny < m and nx >= 0 and ny >= 0:
                    diff.add((nx,ny))
    tot = len(diff)
    print(tot)

def aoc8_2():
    tot = 0
    d = defaultdict(list)
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    n,m = len(g),len(g[0])
    for i in range(n):
        for j in range(m):
            if g[i][j] != '.':
                d[g[i][j]].append((i,j))
    diff = set()
    for _,v in d.items():
        if len(v) == 1:
            continue
        for i in range(len(v)):
            diff.add(v[i])
            for j in range(i+1,len(v)):
                dx = v[j][0] - v[i][0]
                dy = v[j][1] - v[i][1]
                nx,ny = v[j][0] + dx,v[j][1] + dy
                while nx < n and ny < m and nx >= 0 and ny >= 0:
                    diff.add((nx,ny))
                    nx,ny = nx + dx,ny + dy
                nx, ny = v[i][0] - dx, v[i][1] - dy
                while nx < n and ny < m and nx >= 0 and ny >= 0:
                    diff.add((nx,ny))
                    nx,ny = nx - dx,ny - dy
    tot = len(diff)
    print(tot)    
aoc8_2()
