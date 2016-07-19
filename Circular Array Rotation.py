n,k,q = map(int,raw_input().strip().split())
arr = map(int,raw_input().strip().split())
k = k%n
for i in range(q):
    ind = input()
    if ind+k>=0:
        print arr[(ind-k)]
    else:
        print arr[n-abs(ind-k)]