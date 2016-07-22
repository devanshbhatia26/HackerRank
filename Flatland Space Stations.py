n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))
if m==1:
    print n-1
else:
    c.sort()
    maxim = c[0]
    for i in range(m-1):
        temp = (c[i+1]-c[i])/2
        if temp>maxim:
            maxim = temp
    if (n-1)-c[m-1]>maxim:
        maxim = (n-1)-c[m-1]
    print maxim