import sys

def twinArrays(ar1, ar2):
    m1 = min(ar1)
    m2 = min(ar2)
    im1 = []
    for i in range(len(ar1)):
        if ar1[i]==m1:
            im1.append(i)
    im2 = []
    for i in range(len(ar2)):
        if ar2[i]==m2:
            im2.append(i)
    if im1[0]!=im2[0] or len(im1)>1 or len(im2)>1:
        return m1+m2
    t1 = ar1[:]
    t2 = ar2[:]
    t1.remove(m1)
    t2.remove(m2)
    nm1 = min(t1)
    nm2 = min(t2)
    return min(nm1+m2,nm2+m1)
    
    

n = int(raw_input().strip())
ar1 = map(int, raw_input().strip().split(' '))
ar2 = map(int, raw_input().strip().split(' '))
result = twinArrays(ar1, ar2)
print(result)

