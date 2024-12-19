import sys
from collections import defaultdict, Counter
from queue import PriorityQueue
from functools import cache
sys.stdin = open('./day17/input.txt', 'r')
sys.stdout = open('./day17/output.txt', 'w')
sys.setrecursionlimit(10**5)



def aoc17_1():
    ans = []
    A,B,C = 0,0,0
    program = []
    A = int(input().split(':')[-1])
    B = int(input().split(':')[-1])
    C = int(input().split(':')[-1])
    input()
    program = list( map(int,input().split(':')[-1].split(',')))
    # t = list( map(int,input().split(':')[-1].split(',')))
    # for i in range(0,len(t),2):
    #     program.append([t[i],t[i+1]])
    cur_pos = 0
    def combo(val):
        if 0 <= val <= 3:
            return val
        if val == 4:
            return A
        if val == 5:
            return B
        if val == 6:
            return C
    def opt(ins, val):
        nonlocal A,B,C,cur_pos
        if ins == 0:
            A = A // (1 << combo(val))
        elif ins == 1:
            B = B ^ val
        elif ins == 2:
            B = combo(val) % 8
        elif ins == 3:
            if A == 0:
                pass
            else:
                cur_pos = val - 2
        elif ins == 4:
            B = B ^ C
        elif ins == 5:
            ans.append(combo(val) % 8)
        elif ins == 6:
            B = A // (1 << combo(val))
        elif ins == 7:
            C = A // (1 << combo(val))
        

    while cur_pos < len(program):
        ins, val = program[cur_pos], program[cur_pos+1]
        opt(ins,val)
        cur_pos += 2
    print(*ans,sep=',')


def aoc17_2():
    ans = []
    A,B,C = 0,0,0
    program = []
    A = int(input().split(':')[-1])
    B = int(input().split(':')[-1])
    C = int(input().split(':')[-1])
    input()
    program = list( map(int,input().split(':')[-1].split(',')))
    cur_pos = 0
    def combo(val):
        if 0 <= val <= 3:
            return val
        if val == 4:
            return A
        if val == 5:
            return B
        if val == 6:
            return C
    def opt(ins, val):
        nonlocal A,B,C,cur_pos
        if ins == 0:
            A = A // (1 << combo(val))
        elif ins == 1:
            B = B ^ val
        elif ins == 2:
            B = combo(val) % 8
        elif ins == 3:
            if A == 0:
                pass
            else:
                cur_pos = val - 2
        elif ins == 4:
            B = B ^ C
        elif ins == 5:
            ans.append(combo(val) % 8)
        elif ins == 6:
            B = A // (1 << combo(val))
        elif ins == 7:
            C = A // (1 << combo(val))
    
    
    def run(a):
        nonlocal A,B,C,cur_pos,ans
        A = a
        B = 0
        C = 0
        cur_pos = 0
        ans = []
        while cur_pos < len(program):
            ins, val = program[cur_pos], program[cur_pos+1]
            opt(ins,val)
            cur_pos += 2
        return ans.copy()
    def try_bit(solutions, q, ta):
        out = run(ta)
        if len(out) == len(program):
            if all(out[i] == program[i] for i in range(len(out))):
                solutions.append(ta)
        elif len(out) < len(program):
            if all(out[-i] == program[-i] for i in range(1,len(out) + 1)):
                q.append(ta)
    def find():
        solutions = []
        q = []
        q.append(0)
        while len(q):
            a = q.pop()
            for b in range(8):
                ta = (a << 3) | b
                try_bit(solutions, q, ta)
        return min(solutions)

    print(find())

# A的低位影响输出高位，A的高位只影响输出低位
# 3个bit一次循环
def aoc_helper():
    def call(a):
        A,B,C = a,0,0
        out = []
        while A:
            B = A % 8
            B = B ^ 1
            C = A // (1 << B)
            B = B ^ C
            A = A // (8)
            B = B ^ 4
            out.append(B % 8)
        print(out)
    
