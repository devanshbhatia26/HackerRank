n,m = map(int,raw_input().strip().split())
arr = [0]*n
for i in xrange(m):
    a,b,k = map(int,raw_input().strip().split())
    arr[a-1]+=k
    if b!=n:
        arr[b]-=k
init = 0
ans = 0
for i in xrange(n):
    init+=arr[i]
    if init>ans:
        ans = init
print ans