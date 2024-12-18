import sys
from collections import defaultdict, Counter
from queue import PriorityQueue
from functools import cache
sys.stdin = open('./day16/input.txt', 'r')
sys.stdout = open('./day16/output.txt', 'w')
sys.setrecursionlimit(10**5)

INF = 10**9
def aoc16_1():
    g = []
    try:
        while True:
            g.append(list(input()))
    except EOFError:
        pass
    n, m = len(g), len(g[0])
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'S':
                x, y = i, j
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def opt(x, y, cur_dir,score, best_score):
        if g[x][y] == '#' or ((x,y) in best_score and best_score[(x,y)] <= score):
            return INF
        if g[x][y] == 'E':
            return score
        best_score[(x,y)] = score
        res = INF
        for i in range(4):
            dx, dy = dir[(i + cur_dir) % 4]
            nx, ny = x + dx, y + dy
            if i == 0:
                t = opt(nx, ny, (i + cur_dir) % 4, score + 1, best_score)
            elif i == 1 or i == 3:
                t = opt(nx, ny, (i + cur_dir) % 4, score + 1001, best_score)
            else:
                t = INF
            res = min(res, t)
        return res
    result = opt(x, y, 1, 0, {})
    print(result)


def aoc16_2():
    g = []
    try:
        while True:
            g.append(list(input()))
    except EOFError:
        pass
    n, m = len(g), len(g[0])
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'S':
                x, y = i, j
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    routes = []
    def opt(x, y, cur_dir,score, best_score,history:list):
        if g[x][y] == '#' or ((x,y,cur_dir) in best_score and best_score[(x,y,cur_dir)] < score):
            return INF
        if g[x][y] == 'E':
            routes.append((history.copy(), score))
            return score
        best_score[(x,y,cur_dir)] = score
        history.append((x,y))
        res = INF
        for i in range(4):
            dx, dy = dir[(i + cur_dir) % 4]
            nx, ny = x + dx, y + dy
            if i == 0:
                t = opt(nx, ny, (i + cur_dir) % 4, score + 1, best_score, history)
            elif i == 1 or i == 3:
                t = opt(nx, ny, (i + cur_dir) % 4, score + 1001, best_score, history)
            else:
                t = INF
            res = min(res, t)
        history.pop()
        return res
    result = opt(x, y, 1, 0, {},[])
    t = {p for route,score in routes for p in route if score == result}
    print(len(t) + 1)


# 跟上面的代码是一样的，只是用了deque来代替递归
from collections import deque
INF = float('inf')

def aoc16_3():
    g = []
    try:
        while True:
            g.append(list(input()))
    except EOFError:
        pass
    n, m = len(g), len(g[0])
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'S':
                x, y = i, j
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque()
    queue.append((x, y, 1, 0, []))
    best_score = {}
    routes = []
    while queue:
        cx, cy, cur_dir, score, history = queue.popleft()
        if g[cx][cy] == '#' or ((cx, cy, cur_dir) in best_score and best_score[(cx, cy, cur_dir)] < score):
            continue
        if g[cx][cy] == 'E':
            routes.append((history.copy(), score))
            continue
        best_score[(cx, cy, cur_dir)] = score
        history.append((cx, cy))
        for i in range(4):
            dx, dy = dirs[(i + cur_dir) % 4]
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if i == 0:
                    new_score = score + 1
                elif i in [1, 3]:
                    new_score = score + 1001
                else:
                    continue
                queue.append((nx, ny, (i + cur_dir) % 4, new_score, history.copy()))
        history.pop()
    result = min(routes, key=lambda x: x[1])[1]
    t = {p for route, score in routes if score == result for p in route}
    print(len(t) + 1)


aoc16_3()