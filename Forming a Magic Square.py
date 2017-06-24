import sys

def diff(a,b):
    ans = 0
    for i in range(3):
        ans += abs(a[i]-b[i])
    return ans
row = []
for s_i in xrange(3):
    s_temp = map(int,raw_input().strip().split(' '))
    row.append(s_temp)
cols = [[] for i in range(3)]
for i in range(3):
    cols[0].append(row[i][0])
    cols[1].append(row[i][1])
    cols[2].append(row[i][2])
ms = [[8,1,6],[3,5,7],[4,9,2]]
ms2 = [[4,9,2],[3,5,7],[8,1,6]]
c1 = 0
c2 = 0 
c3 = 0
c4 = 0
for r in range(3):
    c1 += diff(row[r],ms[r])
    c2 += diff(row[r],ms2[r])
    c3 += diff(cols[r],ms[r])
    c4 += diff(cols[r],ms2[r])
ans1 = min(c1,c2,c3,c4)
for i in range(3):
    row[i][0],row[i][2] = row[i][2],row[i][0]
    cols[i][0],cols[i][2] = cols[i][2],cols[i][0]
c1 = 0
c2 = 0 
c3 = 0
c4 = 0
for r in range(3):
    c1 += diff(row[r],ms[r])
    c2 += diff(row[r],ms2[r])
    c3 += diff(cols[r],ms[r])
    c4 += diff(cols[r],ms2[r])
ans2 = min(c1,c2,c3,c4)
print min(ans1,ans2)
