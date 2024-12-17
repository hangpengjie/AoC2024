import sys
from collections import defaultdict,Counter
sys.stdin = open('./day3/input.txt', 'r')
sys.stdout = open('./day3/output.txt', 'w')


def aoc3_1():
    tot = 0
    def opt(s:str,l,r):
        if l == r:
            return 0
        if s[l] != '(':
            return 0
        idx = s.find(')',l+1,r)
        t = s[l+1:idx].split(',')
        if len(t) == 2 and t[0].isdigit() and t[1].isdigit() and 4 > len(t[0]) > 0 and 4 > len(t[1]) > 0:
            return int(t[0]) * int(t[1])
        return 0
    try:    
        while True:
            s = input()
            for i in range(len(s) - 2):
                if s[i] == 'm'  and s[i+1] == 'u' and s[i+2] == 'l':
                    tot += opt(s,i+3,len(s))

    except EOFError:
        pass

    print(tot)

def aoc3_2():
    tot = 0
    def opt(s:str,l,r):
        if l == r:
            return 0
        if s[l] != '(':
            return 0
        idx = s.find(')',l+1,r)
        t = s[l+1:idx].split(',')
        if len(t) == 2 and t[0].isdigit() and t[1].isdigit() and 4 > len(t[0]) > 0 and 4 > len(t[1]) > 0:
            return int(t[0]) * int(t[1])
        return 0
    try:    
        start = True
        while True:
            s = input()
            for i in range(len(s) - 2):
                if s[i:].startswith('do()'):
                    start = True
                elif s[i:].startswith("don't()"):
                    start = False
                if start and s[i] == 'm'  and s[i+1] == 'u' and s[i+2] == 'l':
                    tot += opt(s,i+3,len(s))

    except EOFError:
        pass

    print(tot)

aoc3_2()
