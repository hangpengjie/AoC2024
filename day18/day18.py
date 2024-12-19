import sys
from collections import defaultdict, Counter
from queue import PriorityQueue
from functools import cache
sys.stdin = open('./day18/input.txt', 'r')
sys.stdout = open('./day18/output.txt', 'w')
sys.setrecursionlimit(10**5)

def aoc18_1():
    g = []
    n = 71
    z = [[0] * n for _ in range(n)]
    try:
        while True:
            x,y = map(int,input().split(','))
            g.append((x,y))
    except EOFError:
        pass
    for i in range(1024):
        x,y = g[i]
        z[x][y] = 1
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    q = PriorityQueue()
    q.put((0,0,0))
    vis = [[0]*n for _ in range(n)]
    while q:
        step,x,y = q.get()
        if vis[x][y]:
            continue
        vis[x][y] = 1
        if x == n-1 and y == n-1:
            print(step)
            return
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < n and z[nx][ny] == 0:
                q.put((step+1,nx,ny))

def aoc18_2():
    g = []
    n = 71
    z = [[0] * n for _ in range(n)]
    try:
        while True:
            x,y = map(int,input().split(','))
            g.append((x,y))
    except EOFError:
        pass
    
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    vis = [[0]*n for _ in range(n)]
    def find():
        q = []
        q.append((0,0))
        for i in range(n):
            for j in range(n):
                vis[i][j] = 0
        while q:
            x,y = q.pop()
            if vis[x][y]:
                continue
            vis[x][y] = 1
            if x == n-1 and y == n-1:
                return True
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < n and z[nx][ny] == 0:
                    q.append((nx,ny))
        return False
    l,r = 1024,len(g) - 1
    while l < r:
        mid = (l+r)//2
        # for i in range(n):
        #     for j in range(n):
        #         z[i][j] = 0
        for i in range(mid+1):
            x,y = g[i]
            z[x][y] = 1
        if find():
            l = mid + 1
        else:
            r = mid
        for i in range(mid+1):
            x,y = g[i]
            z[x][y] = 0
    print(l)
    print(g[l])

aoc18_2()