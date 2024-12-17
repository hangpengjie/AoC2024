

import sys
from collections import defaultdict,Counter
sys.stdin = open('./day4/input.txt', 'r')
sys.stdout = open('./day4/output.txt', 'w')

def aoc4_1():
    tot = 0
    g = []
    try:
        while True:
            s = input()
            g.append(s)
    except EOFError:
        pass
    dir = [(1,0),(-1,0),(0,1),(0,-1), (1,1),(-1,-1),(-1,1),(1,-1)]
    Q = 'XMAS'
    def f(x,y, idx, d):
        if idx >= 4 or g[x][y] != Q[idx]:
            return 0
        if idx == 3:
            return 1
        res = 0
        for dx,dy in dir:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(g) and 0 <= ny < len(g[0]) and (d == (0,0) or d == (dx,dy)):
                res += f(nx,ny,idx+1,(dx,dy))
        return res
    for i in range(len(g)):
        for j in range(len(g[0])):
            tot += f(i,j,0,(0,0))
    print(tot)

def aoc4_2():
    tot = 0
    g = []
    try:
        while True:
            s = input()
            g.append(s)
    except EOFError:
        pass
    dir = [(-1,-1),(-1,1),(1,-1),(1,1)]
    Q = {'M':0,'S':1}
    def f(x,y):
        d = []
        for dx,dy in dir:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(g) and 0 <= ny < len(g[0]) and g[nx][ny] in Q:
                d.append(Q[g[nx][ny]])
        if(len(d) == 4):
            if d[0] == d[1] and d[1] != d[2] and d[2] == d[3]:
                return 1
            if d[0] == d[2] and d[1] != d[2] and d[1] == d[3]:
                return 1
        return 0
        
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 'A':
                tot += f(i,j)
    print(tot)

aoc4_2()