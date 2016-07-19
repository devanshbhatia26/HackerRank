def ans(arr):
    l = len(arr)
    left = [0]*l
    for i in xrange(1,l):
        left[i]=left[i-1]+arr[i-1]
    right = [0]*l
    for i in xrange(l-1,0,-1):
        right[i-1]=right[i]+arr[i]
    for i in xrange(l):
        if right[i]==left[i]:
            return "YES"
    return "NO"
for i in range(input()):
    n = input()
    arr = map(int,raw_input().strip().split())
    print ans(arr)
        