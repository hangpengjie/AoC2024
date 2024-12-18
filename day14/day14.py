

import sys
from collections import defaultdict,Counter
from functools import cache
sys.stdin = open('./day14/input.txt', 'r')
sys.stdout = open('./day14/output.txt', 'w')
sys.setrecursionlimit(10**6)

def aoc14_1():
    n,m = 103,101
    #n,m = 7, 11
    g = []
    try:
        while True:
            s = input().split()
            x,y = int(s[0].split('=')[-1].split(',')[0]),int(s[0].split('=')[-1].split(',')[1])
            vx,vy = int(s[1].split('=')[-1].split(',')[0]),int(s[1].split('=')[-1].split(',')[1])
            g.append((x,y,vx,vy))
    except EOFError:
        pass
    def opt(x,y,vx,vy,steps):
        if steps==0:
            return (x,y)
        x += vx
        y += vy
        x %= m
        y %= n
        return opt(x,y,vx,vy,steps-1)
    midx = m//2
    midy = n//2
    d = [0] * 4
    for x,y,vx,vy in g:
        x,y = opt(x,y,vx,vy,100)
        if x < midx and y < midy:
            d[0] += 1
        elif x < midx and y > midy:
            d[1] += 1
        elif x > midx and y < midy:
            d[2] += 1
        elif x > midx and y > midy:
            d[3] += 1
    res = 1
    for i in range(4):
        res *= d[i]
    print(res)

# 计算安全系数最小值
def aoc14_2():
    n,m = 103,101
    #n,m = 7, 11
    g = []
    try:
        while True:
            s = input().split()
            x,y = int(s[0].split('=')[-1].split(',')[0]),int(s[0].split('=')[-1].split(',')[1])
            vx,vy = int(s[1].split('=')[-1].split(',')[0]),int(s[1].split('=')[-1].split(',')[1])
            g.append([x,y,vx,vy])
    except EOFError:
        pass
    def opt(x,y,vx,vy,steps):
        if steps==0:
            return (x,y)
        x += vx
        y += vy
        x %= m
        y %= n
        return opt(x,y,vx,vy,steps-1)
    midx = m//2
    midy = n//2
    d = [0] * 4
    for j in range(len(g)):
        x,y,vx,vy = g[j]
        if x < midx and y < midy:
            d[0] += 1
        elif x < midx and y > midy:
            d[1] += 1
        elif x > midx and y < midy:
            d[2] += 1
        elif x > midx and y > midy:
            d[3] += 1
    res = 1
    for i in range(4):
        res *= d[i]
    ans = 0
    for i in range(1,10**4):
        d = [0] * 4
        for j in range(len(g)):
            x,y,vx,vy = g[j]
            x,y = opt(x,y,vx,vy,1)
            if x < midx and y < midy:
                d[0] += 1
            elif x < midx and y > midy:
                d[1] += 1
            elif x > midx and y < midy:
                d[2] += 1
            elif x > midx and y > midy:
                d[3] += 1
            g[j] = [x,y,vx,vy]
        tmp = 1
        for k in range(4):
            tmp *= d[k]
        if tmp < res:
            res = tmp
            ans = i
    
    print(ans)

            
    
aoc14_2()