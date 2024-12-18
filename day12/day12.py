

import sys
from collections import defaultdict,Counter
from functools import cache
sys.stdin = open('./day12/input.txt', 'r')
sys.stdout = open('./day12/output.txt', 'w')
sys.setrecursionlimit(10**6)

def aoc12_1():
    tot = 0
    g = []
    try:
        while True:
            g.append(list(input()))
    except EOFError:
        pass
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    n,m = len(g),len(g[0])
    vis = set()
    diff = 0
    def opt(x,y):
        nonlocal diff
        if (x,y) in vis:
            return
        vis.add((x,y))
        for dx,dy in dir:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and g[nx][ny]==g[x][y]:
                opt(nx,ny)
            else:
                diff += 1
                
    for i in range(n):
        for j in range(m):
            pre_area = len(vis)
            opt(i,j)
            cur_area = len(vis)-pre_area
            tot += cur_area * diff
            diff = 0
    print(tot)

def aoc12_2():
    tot = 0
    g = []
    try:
        while True:
            g.append(list(input()))
    except EOFError:
        pass
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    n,m = len(g),len(g[0])
    vis = set()
    z = []
    diff = 0
    def opt(x,y):
        nonlocal diff
        if (x,y) in vis:
            return
        vis.add((x,y))
        for i,(dx,dy) in enumerate(dir):
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and g[nx][ny]==g[x][y]:
                opt(nx,ny)
            else:
                diff += 1
                z.append((nx,ny,i))
                
    for i in range(n):
        for j in range(m):
            pre_area = len(vis)
            opt(i,j)
            cur_area = len(vis)-pre_area
            z.sort(key=lambda x:(x[2],x[0],x[1]))
            for k in range(1, len(z)):
                if z[k][0] == z[k-1][0] and z[k][1] == z[k-1][1] + 1:
                    diff -= 1
            z.sort(key=lambda x:(x[2],x[1],x[0]))
            for k in range(1, len(z)):
                if z[k][1] == z[k-1][1] and z[k][0] == z[k-1][0] + 1:
                    diff -= 1

            tot += cur_area * diff
            diff = 0
            z.clear()
    print(tot)

aoc12_2()