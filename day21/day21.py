import sys
from collections import defaultdict, Counter,deque
from queue import PriorityQueue
from functools import cache
from itertools import permutations
sys.stdin = open('./day21/input.txt', 'r')
sys.stdout = open('./day21/output.txt', 'w')
sys.setrecursionlimit(10**5)
INF = 10**9

nums_button = [ ['7','8','9'],
                ['4','5','6'],
                ['1','2','3'],
                ['#','0','A']]

dirs_button = [['#','^','A'],
               ['<','v','>']]
dirs = [(0,1,'>'),(1,0,'v'),(0,-1,'<'),(-1,0,'^')]
def aoc21_1():
    g = []
    try:
        while True:
            g.append(list(input()))
    except EOFError:
        pass
    
    def opt_nums(v:list):
        n,m = len(nums_button),len(nums_button[0])
        x,y = n-1,m-1
        vis = set()
        paths = []
        def search(cx,cy,tar,path):
            nonlocal x,y
            if nums_button[cx][cy] == tar:
                x,y = cx,cy
                path.append('A')
                paths.append(path.copy())
                path.pop()
                return
            if (cx,cy) in vis:
                return
            vis.add((cx,cy))
            for dx,dy,op in dirs:
                nx,ny = cx+dx,cy+dy
                if 0<=nx<n and 0<=ny<m and nums_button[nx][ny] != '#':
                    path.append(op)
                    search(nx,ny,tar,path)
                    path.pop()
            vis.remove((cx,cy))
            return
        ans = []
        for t in v:
            cx,cy = x,y
            search(cx,cy,t,path=[])
            tmp = []
            cnt = 10**9
            for p in paths:
                cnt = min(cnt,len(p))
            for p in paths:
                if len(p) == cnt:
                    tmp.append(p)
            if ans:
                r = []
                for i in range(len(ans)):
                    for p in tmp:
                        d = ans[i].copy()
                        d.extend(p)
                        r.append(d)
                ans = r   
            else:
                ans = tmp.copy()
            paths = []
        
        return ans
            
    def opt_dirs(v:list):
        n,m = len(dirs_button),len(dirs_button[0])
        x,y = 0,m-1
        vis = set()
        paths = []
        def search(cx,cy,tar,path):
            nonlocal x,y
            if dirs_button[cx][cy] == tar:
                x,y = cx,cy
                path.append('A')
                paths.append(path.copy())
                path.pop()
                return
            if (cx,cy) in vis:
                return
            vis.add((cx,cy))
            for dx,dy,op in dirs:
                nx,ny = cx+dx,cy+dy
                if 0<=nx<n and 0<=ny<m and dirs_button[nx][ny] != '#':
                    path.append(op)
                    search(nx,ny,tar,path)
                    path.pop()
            vis.remove((cx,cy))
            return
        ans = []
        for t in v:
            cx,cy = x,y
            search(cx,cy,t,path=[])
            tmp = []
            cnt = 10**9
            for p in paths:
                cnt = min(cnt,len(p))
            for p in paths:
                if len(p) == cnt:
                    tmp.append(p)
            if ans:
                r = []
                for i in range(len(ans)):
                    for p in tmp:
                        d = ans[i].copy()
                        d.extend(p)
                        r.append(d)
                ans = r   
            else:
                ans = tmp.copy()
            paths = []
        
        return ans
    def opt(v:list):
        ans = []
        for x in v:
            t = opt_dirs(x)
            ans.extend(t)
        cnt = 10**9
        for x in ans:
            cnt = min(cnt,len(x))
        tmp = []
        for x in ans:
            if len(x) == cnt:
                tmp.append(x)
        ans = tmp
        # for x in ans:
        #     print(''.join(x))
        return ans
            
    def slove(a,b):
        z = [a,b]
        tmp = opt_nums(z)
        r = opt(opt(tmp))
        return len(r[0])
    tot = 0
    # 间接的方式
    for x in g:
        ps = slove('A',x[0]) - 1
        for t in range(1, len(x), 1):
            ps += slove(x[t-1],x[t]) - slove('A',x[t-1]) + 1
        print(ps)
        tot += ps * int(''.join(x[:len(x)-1]))
    print(tot)


def aoc21_2():
    # https://tio.run/##lVZLc9s2EL7zV2wnB5IxraEkPzWmW11y7PSQm8bmMCJkcUKBKgDZUjr57eouAIIgS7sTHWzw291vn3jsT2rb8Pn5vBHNDjYHvlZNU0uodvtGKKjFIV8X6y0LtLwQL/tCSNaKl@LlsGNc/UWgSOBLVbOvpz0LgqBkG9CW0SZeBIA/wdRB8I4y2hVHWf1g2Z8NZzGqWSvtIZJi3bdb1RVnsGkE6EXFAVUmcl9XigAZxVBtjOy3DMLwydKVlVQFXyOjKoRKgPGyT4zAKn2CS9AKuNQ6q2kHTYmLY6aiWufrphElZPCP5giX4QKiWQLzODFASsDUA6YEpAnMWmBmNRwwtxwOuLIm0xa4tiYOuLEmDri1JmkL3FkTB9xbkzQOfgaBTiO3Sbl0TCYLSstYmUwWlJYFdCYLSqvT0MCsBWYWmHsmUwKuPBMNXHsmGrjxTFICbj0TDdx5Jhq4DymdoKwEW6uq4e81yNXheViYx2EtX4fVfnD96ErnHPaKlw6Lp4HnYZ6Pw0q8Dmv1YNL6w@w@GuRd88qibwelGp4AZ0eVuw/TRTvWuAuMALLM1zNSb/AxzqC1sBSdjrFxxexNv1MylWi9QW@mtBKrJXuXc9Cyj1mdsgl5UwmpHJNPvDIfT1pNpz@q5RXGqJbHBMqTDsseGJ6PxGOKXdHKIzxmkHYJUovyI3Jgg@EzykeK0Ok8kM4lKjm@0xgfxYTzQXyn9/i0zrPhO/nxZT0@23hrcqEnwDAa7@9rH622PTjloVbossZSRbHGPmFLeAlqy9rpe6vUVn8fTQuh2fjjCIVVPzmxJWrHGmOqFLAjOpFtSlHXB31Sez3CYzqma8EfHz8ZinlS7Pd4uEcuJ78UtrGfQFa7qi6EvmxOzrPvilx7kfyq51Pr@TjwjH7eGHznzRvgpYglrGv4xkDWzRvdr4KRFValDapmPDL8Md16M8CIsesP/TbabpkF3XXoiaavkroBml0qUA28MP0PQwK68EfGbcg2NWyvms3EiaQFp3EM/GvW6PePNHSXS/b3geF2yzGXF7WN2m/sP3ebfuSM86Tjc0u1aclsgdtP2i2Y4oUDtFQ1qqhRlJoTBks5ctpSn39Uey/MdrWaLp7iLgrDdpGNJvn/Z3niiD78@VW4BLxNvhTYrtgvvA7EPoYUPs5wZksW0Z9eiW3oJkAYD/s/RlhC9PlVHPouLclnVFXaaLW4xD1ig9gVFdeoHAvAUsjDLvooWt0fgs3GQzKixwdqrt@PAjPov07xnOqkk6Is88LKoxBfkuEHYs9viB1CgczC33FJAWaYI94cbFPgeGczjAKHM895sWN5TpMZ5jllnOehSZDMMTrPm/5H/qQ9TPeCCqfrZF7DJJvQkzjR5hO/EnFwPp/T2f0yuL9Ll8H0FldX1zfLYI6rfwE
    pass