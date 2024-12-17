import sys
from collections import defaultdict,Counter
sys.stdin = open('./day2/input.txt', 'r')
sys.stdout = open('./day2/output.txt', 'w')


def aoc2_1():
    tot = 0
    try:
        while True:
            g = list(map(int,input().split()))
            t = []
            for i in range(1, len(g)):
                t.append(g[i]-g[i-1])
            if all(x > 0 for x in t):
                if all(x <= 3 for x in t):
                    tot += 1
            if all(x < 0 for x in t):
                if all(x >= -3 for x in t):
                    tot += 1
    except EOFError:
        pass
    print(tot)


def aoc2_2():
    tot = 0
    def check(g):
        t = []
        for i in range(1, len(g)):
            t.append(g[i]-g[i-1])
        if all(x > 0 for x in t):
            if all(x <= 3 for x in t):
                return True
        
        if all(x < 0 for x in t):
            if all(x >= -3 for x in t):
                return True
        return False
        
    try:
        while True:
            g = list(map(int,input().split()))
            for i in range(len(g)):
                if check(g[:i]+g[i+1:]):
                    tot += 1
                    break
            
    except EOFError:
        pass
    print(tot)
aoc2_2()