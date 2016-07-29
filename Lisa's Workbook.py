n,k = map(int,raw_input().strip().split())
arr = map(int,raw_input().strip().split())
page=1
count=0
for a in arr:
    flag = True
    for i in range(1,a+1):
        if i==page:
            count+=1
        if (i%k)==0:
            page+=1
            if i==a:
                flag = False
    if flag:
        page+=1
print count