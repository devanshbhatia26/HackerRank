g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split())
    c = 0
    i = 0
    ptr = 0
    while i<n:
        while i<n and arr[i]<=arr[ptr]:
            i+=1
        if not i==n:
            c+=1
            ptr=i
    if not c%2:
        print "BOB"
    else:
        print "ANDY"
