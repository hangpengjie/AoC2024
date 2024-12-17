import sys
from collections import defaultdict,Counter
sys.stdin = open('./day1/input.txt', 'r')
sys.stdout = open('./day1/output.txt', 'w')

def aoc1_1():
    
    l,r = [],[]
    try:
        while True:
            s = input().split()
            l.append(int(s[0]))
            r.append(int(s[1]))
    except EOFError:
        pass
    l.sort()
    r.sort()
    tot = 0
    for a,b in zip(l,r):
        tot += abs(a-b)
    print(tot)

def aoc1_2():
    l,r = [],Counter()
    try:
        while True:
            s = input().split()
            l.append(int(s[0]))
            r[int(s[1])] += 1
    except EOFError:
        pass
    tot = 0
    for x in l:
        tot += x * r[x]
    print(tot)

aoc1_2()