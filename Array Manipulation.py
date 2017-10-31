n, m = map(int, raw_input().strip().split())
arr = [0 for _ in xrange(n+2)]

for _ in xrange(m):
    i, j, k = map(int, raw_input().strip().split())
    arr[i] += k
    arr[j + 1] -= k

for i in xrange(1, n+1):
    arr[i] += arr[i-1]

print arr[arr.index(max(arr))]