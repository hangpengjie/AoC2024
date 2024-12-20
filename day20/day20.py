import sys
from collections import defaultdict, Counter,deque
from queue import PriorityQueue
from functools import cache
sys.stdin = open('./day20/input.txt', 'r')
sys.stdout = open('./day20/output.txt', 'w')
sys.setrecursionlimit(10**5)
INF = 10**9


def aoc20_1():
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    n,m = len(g), len(g[0])
    x,y = 0,0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'S':
                x,y = i,j
                break
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    def opt0(x,y):
        q = PriorityQueue()
        q.put((0,x,y))
        vis = [[False] * m for _ in range(n)]
        while q:
            steps,x,y = q.get()
            if vis[x][y]:
                continue
            vis[x][y] = True
            if g[x][y] == 'E':
                return steps
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#':
                    q.put((steps+1,nx,ny))
        return -1
    z = opt0(x,y)
    def opt1_iterative(x, y, n, m, g):
        outs = []
        vis = [[False] * m for _ in range(n)]
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]  # assuming these are defined
        
        # Stack will store: (x, y, is_cheat, steps, is_backtrack)
        stack = [(x, y, False, 0, False)]
        
        while stack:
            x, y, is_cheat, steps, is_backtrack = stack.pop()
            
            if is_backtrack:
                vis[x][y] = False
                continue
                
            if vis[x][y]:
                continue
                
            if g[x][y] == 'E':
                if is_cheat:
                    outs.append(steps)
                continue
                
            vis[x][y] = True
            stack.append((x, y, is_cheat, steps, True))  # Add backtrack marker
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if g[nx][ny] == '#':
                        if not is_cheat:  # Only proceed if not already cheating
                            stack.append((nx, ny, True, steps + 1, False))
                    else:
                        stack.append((nx, ny, is_cheat, steps + 1, False))
        
        return outs
    outs = opt1_iterative(x, y, n, m, g)
    # outs = []
    # vis = [[False] * m for _ in range(n)]
    # def opt1(x,y,is_cheat,steps):
    #     if vis[x][y]:
    #         return
    #     if g[x][y] == 'E':
    #         if is_cheat:
    #             outs.append(steps)
    #         return
    #     vis[x][y] = True
    #     for dx,dy in dirs:
    #         nx,ny = x+dx,y+dy
    #         if 0 <= nx < n and 0 <= ny < m :
    #             if g[nx][ny] == '#' :
    #                 if is_cheat:
    #                     continue
    #                 else:
    #                     opt1(nx,ny,True,steps+1)
    #             else:
    #                 opt1(nx,ny,is_cheat,steps+1)
    #     vis[x][y] = False
    # opt1(x,y,False,0)
    # print(outs)
    tot = 0
    for x in outs:
        if z - x >= 100:
            tot += 1
    print(tot)




def aoc20_2():
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    n,m = len(g), len(g[0])
    x,y = 0,0
    ex,ey = 0,0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'S':
                x,y = i,j
            if g[i][j] == 'E':
                ex,ey = i,j
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    def opt0(x,y):
        q = PriorityQueue()
        q.put((0,x,y))
        vis = [[False] * m for _ in range(n)]
        while q:
            steps,x,y = q.get()
            if vis[x][y]:
                continue
            vis[x][y] = True
            if g[x][y] == 'E':
                return steps
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#':
                    q.put((steps+1,nx,ny))
        return -1
    z = opt0(x,y)
    
    dis = [[INF] * m for _ in range(n)]
    dis[ex][ey] = 0
    q = deque([(ex,ey)])
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#' and dis[nx][ny]  > dis[x][y] + 1:
                dis[nx][ny] = dis[x][y] + 1
                q.append((nx,ny))

    def opt1_iterative(x, y, n, m, g):
        outs = []
        vis = [[False for _ in range(m)] for _ in range(n)]
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]  # assuming these are defined
        
        # Stack will store: (x, y, is_cheat, steps, is_backtrack)
        stack = [(x, y, 0, 0, False)]
        
        while stack:
            x, y, cheats, steps, is_backtrack = stack.pop()
            
            if is_backtrack:
                vis[x][y] = False
                continue
                
            if vis[x][y]:
                continue
                
            if g[x][y] == 'E':
                outs.append(steps)
                continue
                
            vis[x][y] = True
            stack.append((x, y, cheats, steps, True))  # Add backtrack marker
            if cheats:
                pass
            else:
                mx = 20
                for dx in range(-mx,mx+1,1):
                    for dy in range(-mx,mx+1,1):
                        t = abs(dx) + abs(dy)
                        if t <= mx:
                            nx,ny = x+dx,y+dy
                            if 0 <= nx < n and 0 <= ny < m:
                                if g[nx][ny] == '#':
                                    continue
                                else:
                                    outs.append(dis[nx][ny] + steps + t)
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if g[nx][ny] == '#':
                            continue
                        else:
                            stack.append((nx, ny, cheats, steps + 1, False))
        
        return outs
    outs = opt1_iterative(x, y, n, m, g)
    # print(outs)
    # c = Counter(outs)
    # print(c)
    tot = 0
    for x in outs:
        if z - x >= 100:
            tot += 1
    print(tot)
    print(1008542)

aoc20_2()