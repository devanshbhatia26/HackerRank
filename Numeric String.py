import sys

def getMagicNumber(s, k, b, m):
    d = map(int,list(s))
    last = int(s[:k],b)
    p = pow(b,k-1,m)
    ps = []
    ans = last%m
    for i in xrange(1,len(s)-k+1):
        last =  ((b)*(last-p*d[i-1])+d[i+k-1])%m
        ans += last
    return ans

s = raw_input().strip()
k, b, m = raw_input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)

