n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
flag = 1
i = 0
count =0
while flag:
    if i!=n-2 and (c[i+1]==1 or c[i+2]==0):
        i=i+2
        count+=1
    else:
        i+=1
        count+=1
    if i==n-1:
        flag = 0
print count