

import sys
from collections import defaultdict,Counter
sys.stdin = open('./day6/input.txt', 'r')
sys.stdout = open('./day6/output.txt', 'w')
sys.setrecursionlimit(10**6)

def aoc6_1():
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
    path = set()
    def opt(x,y,cur_dir):
        path.add((x,y))
        nx,ny = x + dir[cur_dir][0],y + dir[cur_dir][1]
        if 0 <= nx < n and 0 <= ny < m:
            if g[nx][ny] == '.' or g[nx][ny] == '^':
                opt(nx,ny,cur_dir)
            elif g[nx][ny] == '#':
                opt(x,y,(cur_dir + 1) % 4)
        else:
            return

    for i in range(n):
        for j in range(m):
            if g[i][j] == '^':
                opt(i,j,3)
                break
    tot = len(path)
    print(tot)

def aoc6_2():
    tot = 0
    g = []
    try:
        while True:
            s = input()
            g.append(list(s))
    except EOFError:
        pass
    n,m = len(g),len(g[0])
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    path = set()
    def opt(x,y,cur_dir):
        nx,ny = x + dir[cur_dir][0],y + dir[cur_dir][1]
        if 0 <= nx < n and 0 <= ny < m:
            if g[nx][ny] == '.' or g[nx][ny] == '^':
                return opt(nx,ny,cur_dir)
            elif g[nx][ny] == '#':
                if (nx,ny,cur_dir) not in path:
                    path.add((nx,ny, cur_dir))
                else:
                    return 1
                return opt(x,y,(cur_dir + 1) % 4)
        return 0
    x,y = 0,0
    for i in range(n):
        for j in range(m):
            if g[i][j] == '^':
                x,y = i,j
                break
    for i in range(n):
        for j in range(m):
            if g[i][j] == '.':
                path.clear()
                g[i][j] = '#'
                tot += opt(x,y,3)
                g[i][j] = '.'
    print(tot)

aoc6_2()