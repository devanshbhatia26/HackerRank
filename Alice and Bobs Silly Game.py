p = [0]*(10**5)
for i in range(2,10**5):
    if p[i]==0:
        p[i]=2
        for j in range(2*i,10**5,i):
            p[j]=1

g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    temp = p[:n+1].count(2)
    if temp%2:
        print "Alice"
    else:
        print "Bob"
