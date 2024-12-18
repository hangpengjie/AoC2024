

import sys
from collections import defaultdict,Counter
sys.stdin = open('./day10/input.txt', 'r')
sys.stdout = open('./day10/output.txt', 'w')
sys.setrecursionlimit(10**6)

def aoc10_1():
    tot = 0
    g = []
    try:
        while True:
            s = input()
            g.append(s)
    except EOFError:
        pass
    n,m = len(g),len(g[0])
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    vis = set()
    def opt(x,y,cur):
        if cur == 9:
            vis.add((x,y))
        for dx,dy in dir:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and int(g[nx][ny]) == cur+1:
                opt(nx,ny,cur+1)
        return 
    for i in range(n):
        for j in range(m):
            if g[i][j] == '0':
                opt(i,j,0)
                tot += len(vis)
                vis.clear()
    print(tot)

def aoc10_2():
    tot = 0
    g = []
    try:
        while True:
            s = input()
            g.append(s)
    except EOFError:
        pass
    n,m = len(g),len(g[0])
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    def opt(x,y,cur):
        if cur == 9:
            return 1
        res = 0
        for dx,dy in dir:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and int(g[nx][ny]) == cur+1:
                res += opt(nx,ny,cur+1)
        return res
    for i in range(n):
        for j in range(m):
            if g[i][j] == '0':
                tot += opt(i,j,0)

    print(tot)

aoc10_2()