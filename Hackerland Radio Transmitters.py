import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
x = sorted(map(int,raw_input().strip().split(' ')))
ptr = x[0]
i = 1
ans = 0
if n==1:
    print 1
    print sys.exit(1)
while i<n:
    while i<n and x[i]-ptr<=k:
        i+=1
    ptr = x[i-1]
    ans+=1
    while i<n and x[i]-ptr<=k:
        i+=1
    if i>=n:
        break
    ptr = x[i]
print ans     


