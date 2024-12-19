import sys
from collections import defaultdict, Counter
from queue import PriorityQueue
from functools import cache
sys.stdin = open('./day19/input.txt', 'r')
sys.stdout = open('./day19/output.txt', 'w')
sys.setrecursionlimit(10**5)
INF = 10**9
def aoc19_1():
    g = input().split(', ')
    input()
    z = []
    try:
        while True:
            z.append(input())
    except EOFError:
        pass
    def check(s:str):
        n = len(s)
        m = len(g)
        dp = [[INF] * (m+1) for _ in range(n+1)]
        for i in range(m + 1):
            dp[0][i] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if len(g[j - 1]) <= i:
                    if s[:i].endswith(g[j - 1]):
                        dp[i][j] = min(dp[i][j], min(dp[i-len(g[j-1])]) + 1)
                dp[i][j] = min(dp[i][j], dp[i][j-1])
        return dp[n][m] < INF
 
    tot = 0
    for x in z:
        if check(x):
            tot += 1
    print(tot)

def aoc19_2():
    g = input().split(', ')
    input()
    z = []
    try:
        while True:
            z.append(input())
    except EOFError:
        pass
    def check(s:str):
        n = len(s)
        m = len(g)
        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if len(g[j - 1]) <= i:
                    if s[:i].endswith(g[j - 1]):
                        dp[i][j] += sum(dp[i-len(g[j-1])])
        return sum(dp[n])
 
    tot = 0
    for x in z:
        tot += check(x)
    print(tot)


# part2 另一种方法
def aoc19_2_1():
    g = input().split(', ')
    input()
    z = []
    try:
        while True:
            z.append(input())
    except EOFError:
        pass
    def check(s:str):
        n = len(s)
        m = len(g)
        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[0] = [1] * (m+1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if len(g[j - 1]) <= i:
                    if s[:i].endswith(g[j - 1]):
                        dp[i][j] += dp[i-len(g[j-1])][-1]
                dp[i][j] += dp[i][j-1]
        return dp[n][-1]
 
    tot = 0
    for x in z:
        tot += check(x)
    print('right answer:',615388132411142)
    print(tot)


aoc19_2_1()