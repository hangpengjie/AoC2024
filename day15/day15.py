

import sys
from collections import defaultdict,Counter
from functools import cache
sys.stdin = open('./day15/input.txt', 'r')
sys.stdout = open('./day15/output.txt', 'w')
sys.setrecursionlimit(10**6)


# 段错误  
# def aoc15_1():
#     tot = 0
#     g = []
#     instructions = []
#     try:
#         while True:
#             s = input()
#             if len(s) == 0:
#                 break
#             else:
#                 g.append(list(s))
#         while True:
#             s = input()
#             instructions.extend(list(s))
#     except EOFError:
#         pass
#     dir = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}
#     n,m = len(g),len(g[0])
#     s_x,s_y = 0,0
#     def opt0(x,y,dx,dy):
#         nx,ny = x+dx,y+dy
#         if nx < n and ny < m and nx >= 0 and ny >= 0:
#             if g[nx][ny] == 'O':
#                 opt0(nx,ny,dx,dy)
#             if g[nx][ny] == '.':
#                 g[nx][ny],g[x][y] = g[x][y],g[nx][ny]
#         return
#     def opt(x,y,steps):
#         if steps == len(instructions):
#             return
#         dx,dy = dir[instructions[steps]]
#         nx,ny = x+dx,y+dy
#         if nx < n and ny < m and nx >= 0 and ny >= 0:
#             if g[nx][ny] == 'O':
#                 opt0(nx,ny,dx,dy)
#             if g[nx][ny] == '.':
#                 g[nx][ny],g[x][y] = g[x][y],g[nx][ny]
#                 opt(nx,ny,steps+1)
#             else:
#                 opt(x,y,steps+1)

#     for i in range(n):
#         for j in range(m):
#             if g[i][j] == '@':
#                 s_x,s_y = i,j
#                 break
#     opt(s_x,s_y,0)
#     for i in range(n):
#         for j in range(m):
#             if g[i][j] == 'O':
#                 tot += 100 * i + j
#     print(tot)


def aoc15_1():
    tot = 0
    g = []
    instructions = []
    try:
        while True:
            s = input()
            if len(s) == 0:
                break
            else:
                g.append(list(s))
        while True:
            s = input()
            instructions.extend(list(s))
    except EOFError:
        pass
    dir = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}
    n,m = len(g),len(g[0])
    s_x,s_y = 0,0
    def opt0(x,y,dx,dy):
        nx,ny = x+dx,y+dy
        if nx < n and ny < m and nx >= 0 and ny >= 0:
            if g[nx][ny] == 'O':
                opt0(nx,ny,dx,dy)
            if g[nx][ny] == '.':
                g[nx][ny],g[x][y] = g[x][y],g[nx][ny]
        return

    for i in range(n):
        for j in range(m):
            if g[i][j] == '@':
                s_x,s_y = i,j
                break
    x,y = s_x,s_y
    for p in instructions:
        dx,dy = dir[p]
        nx,ny = x+dx,y+dy
        if nx < n and ny < m and nx >= 0 and ny >= 0:
            if g[nx][ny] == 'O':
                opt0(nx,ny,dx,dy)
            if g[nx][ny] == '.':
                g[nx][ny],g[x][y] = g[x][y],g[nx][ny]
                x,y = nx,ny
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'O':
                tot += 100 * i + j
    print(tot)

def aoc15_2():
    tot = 0
    g = []
    instructions = []
    try:
        while True:
            s = input()
            if len(s) == 0:
                break
            else:
                z = []
                for i in range(len(s)):
                    if s[i] == '@':
                        z.append('@')
                        z.append('.')
                    elif s[i] == 'O':
                        z.append('[')
                        z.append(']')
                    else:
                        z.append(s[i])
                        z.append(s[i])
                g.append(z)
        while True:
            s = input()
            instructions.extend(list(s))
    except EOFError:
        pass
    
    dir = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}
    n,m = len(g),len(g[0])
    s_x,s_y = 0,0
    def get_whole(x,y):
        fx,fy=0,0
        if g[x][y] == '[':
            fx,fy = x,y+1
            return (x,y,fx,fy)
        else:
            fx,fy = x,y-1
            return (fx,fy,x,y)
    # def opt0(x,y,dx,dy):
    #     if g[x][y] == '.':
    #         return
    #     nx,ny = x+dx,y+dy

    #     if dx == 0:
    #         if g[nx][ny] in '[]':
    #             opt0(nx,ny,dx,dy)
    #         if g[nx][ny] == '.':
    #             g[nx][ny],g[x][y] = g[x][y],g[nx][ny]
    #     else:
    #         vis = set()
    #         vis.add(get_whole(x,y))
    #         tmp = set()
    #         flg = True
    #         for x,y,fx,fy in vis:
    #             nx,ny,nfx,nfy = x+dx,y+dy,fx+dx,fy+dy
    #             if g[nx][ny] == '#' or g[nfx][nfy] == '#':
    #                 return
    #             elif g[nx][ny] in '[]' and g[nfx][nfy] in '[]':
    #                 tmp.add(get_whole(nx,ny))
    #                 tmp.add(get_whole(nfx,nfy))
    #                 flg = False
            
    #         if flg:
    #             for x,y,fx,fy in vis:
    #                 nx,ny,nfx,nfy = x+dx,y+dy,fx+dx,fy+dy
    #                 g[x][y],g[nx][ny] = g[nx][ny],g[x][y]
    #                 g[fx][fy],g[nfx][nfy] = g[nfx][nfy],g[fx][fy]
    #         else:
    #     return


    def opt1(x,y,dx,dy):
        nx,ny = x+dx,y+dy
        if g[nx][ny] in '[]':
            opt1(nx,ny,dx,dy)
        if g[nx][ny] == '.':
            g[nx][ny],g[x][y] = g[x][y],g[nx][ny]
    
    def opt2(cur:set,dx,dy):
        tmp = set()
        flg = True
        for x,y,fx,fy in cur:
            nx,ny = x+dx,y+dy
            nfx,nfy = fx+dx,fy+dy
            if g[nx][ny] == '#' or g[nfx][nfy] == '#':
                return
            if g[nx][ny] in '[]':
                tmp.add(get_whole(nx,ny))
                flg = False
            if g[nfx][nfy] in '[]':
                tmp.add(get_whole(nfx,nfy))
                flg = False
        
        if flg:
            for x,y,fx,fy in cur:
                nx,ny = x+dx,y+dy
                nfx,nfy = fx+dx,fy+dy
                g[x][y],g[nx][ny] = g[nx][ny],g[x][y]
                g[fx][fy],g[nfx][nfy] = g[nfx][nfy],g[fx][fy]
        else:
            opt2(tmp,dx,dy)
            for x,y,fx,fy in cur:
                nx,ny = x+dx,y+dy
                nfx,nfy = fx+dx,fy+dy
                if g[nx][ny] != '.' or g[nfx][nfy] != '.':
                    return
            for x,y,fx,fy in cur:
                nx,ny = x+dx,y+dy
                nfx,nfy = fx+dx,fy+dy
                g[x][y],g[nx][ny] = g[nx][ny],g[x][y]
                g[fx][fy],g[nfx][nfy] = g[nfx][nfy],g[fx][fy]
    def opt0(cur:set,dx,dy):
        if dx == 0:
            x,y = cur.pop()
            opt1(x,y,dx,dy)
        else:
            x,y = cur.pop()
            cur.add(get_whole(x,y))
            opt2(cur,dx,dy)
                

        return

    for i in range(n):
        for j in range(m):
            if g[i][j] == '@':
                s_x,s_y = i,j
                break
    x,y = s_x,s_y
    for p in instructions:
        dx,dy = dir[p]
        nx,ny = x+dx,y+dy
        if nx < n and ny < m and nx >= 0 and ny >= 0:
            if g[nx][ny] in '[]':
                opt0(set([(nx,ny)]),dx,dy)
            if g[nx][ny] == '.':
                g[nx][ny],g[x][y] = g[x][y],g[nx][ny]
                x,y = nx,ny
    for i in range(n):
        for j in range(m):
            if g[i][j] == '[':
                tot += 100 * i + j
    print(tot)

aoc15_2()