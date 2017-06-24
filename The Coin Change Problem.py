import sys

def getWays(n, c , m):
    table = [[0]*(n+1) for i in range(m)]
    for i in range(m):
        table[i][0]=1
    for i in range(1,n+1):
        for j in range(m):
            if i>=c[j]:
                table[j][i] += table[j][i-c[j]]
            if j>0:
                table[j][i] += table[j-1][i]
    return table[m-1][n]
    

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(long, raw_input().strip().split(' '))
ways = getWays(n, c, m)
print ways
