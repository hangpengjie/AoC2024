

import sys
from collections import defaultdict,Counter
sys.stdin = open('./day9/input.txt', 'r')
sys.stdout = open('./day9/output.txt', 'w')
sys.setrecursionlimit(10**6)


def aoc9_1():
    tot = 0
    z = input()
    n = len(z)
    idx = 0
    v = []
    for i in range(0,n,2):
        for _ in range(int(z[i])):
            v.append(idx)
        if i + 1 < n:
            for _ in range(int(z[i+1])):
                v.append(-1)
        idx += 1
    l = 0
    r = len(v) - 1
    while l < r:
        while l < r and v[l] != -1:
            l += 1
        while l < r and v[r] == -1:
            r -= 1
        if l < r:
            v[l],v[r] = v[r],v[l]
            l,r = l+1,r-1
    for i,x in enumerate(v):
        if x >= 0:
            tot += i * x
        else:
            break
    print(tot)

def aoc9_2():
    tot = 0
    z = input()
    n = len(z)
    idx = 0
    v = []
    free = []
    for i in range(0,n,2):
        for _ in range(int(z[i])):
            v.append(idx)
        if i + 1 < n:
            free.append([len(v), int(z[i+1])])
            for _ in range(int(z[i+1])):
                v.append(-1)
            
        idx += 1
    
    l = 0
    r = len(v) - 1
    while r >= 0:
        if r >= 0 and v[r] == -1:
            r -= 1
        elif r >= 0:
            cnt = 0
            l = r
            while l >= 0 and v[l] == v[r]:
                cnt += 1
                l -= 1
            for e in free:
                if e[0] < r and e[1] >= cnt:
                    for i in range(e[0], e[0] + cnt):
                        v[i],v[r] = v[r],v[i]
                        r -= 1
                    e[0] += cnt
                    e[1] -= cnt
                    break
                if e[0] >= r:
                    break
            r = l


    for i,x in enumerate(v):
        if x >= 0:
            tot += i * x

    print(tot)
aoc9_2()