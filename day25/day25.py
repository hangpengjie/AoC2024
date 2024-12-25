import sys
from collections import defaultdict, Counter,deque
from queue import PriorityQueue
from functools import cache
from itertools import permutations
sys.stdin = open('./day25/input.txt', 'r')
sys.stdout = open('./day25/output.txt', 'w')
sys.setrecursionlimit(10**5)

def aoc25_1():
    g = []
    try:
        while True:
            z = []
            g.append(z)
            while True:
                s = input()
                if len(s) == 0:
                    break
                else:
                    z.append(s)
            

    except EOFError:
        pass
    lock = []
    key = []
    def is_lock(x):
        return x[0][0] == '#'
    def opt_lock(x):
        res = [0] * len(x[0])
        for j in range(len(x[0])):
            for i in range(len(x)):
                if x[i][j] == '#':
                    res[j] += 1
                else:
                    break
        return res
    def opt_key(x):
        res = [0] * len(x[0])
        for j in range(len(x[0])):
            for i in range(len(x)-1,-1,-1):
                if x[i][j] == '#':
                    res[j] += 1
                else:
                    break
        return res
    for z in g:
        if is_lock(z):
            lock.append(opt_lock(z))
        else:
            key.append(opt_key(z))
    m = 7
    n = 5
    tot = 0
    for a in key:
        for b in lock:
            if all(a[i] + b[i] <= m for i in range(n)):
                tot += 1

    print(tot)

aoc25_1()
