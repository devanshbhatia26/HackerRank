#!/bin/python
from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

n,k,m = raw_input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]

component = defaultdict(int)
graph = defaultdict(list)

for a0 in xrange(k):
    x,y = raw_input().strip().split(' ')
    x,y = [int(x),int(y)]
    graph[x].append(y)
    graph[y].append(x)

a = map(int, raw_input().strip().split(' '))

vis = defaultdict(bool)

c = 1

def explore(v,c):
    vis[v] = True
    component[v] = c
    for i in graph[v]:
        if not vis[i]:
            explore(i,c)

for v in a:
    if not vis[v]:
        explore(v,c)
        c += 1


def find(a):
    return component[a]

def lps(string):
    n = len(string)
    L = [[0]*n for x in range(n)]
    for i in range(n):
        L[i][i] = 1
    for c in range(2, n+1):
        for i in range(n-c+1):
            j = i+c-1
            #print string[i]
            #print find(string[i])
            #print string[j]
            #print find(string[j])
            if find(string[i])==find(string[j]) and c == 2:
                L[i][j] = 2
            elif find(string[i]) == find(string[j]):
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);
    return L[0][n-1]

print lps(a)
