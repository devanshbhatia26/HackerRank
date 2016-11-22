n = input()
arr = map(int,raw_input().strip().split())
score = [0]*n
def prev(start,dec):
    if start-(dec-1)>=0:
        return (start-(dec-1),start)
    else:
        return (0,start,n-((dec-1)-start),n-1)
for i in xrange(n):
    if arr[i]!=0:
        temp = prev(i,arr[i])
        #print temp
        score[temp[0]]-=1
        if temp[1]+1<n:
            score[temp[1]+1]+=1
        if len(temp)==4:
            score[temp[2]]-=1
        #print score
maxs = score[0]
s = score[0]
ans = 0
for i in range(1,n):
    s+=score[i]
    if maxs<s:
        maxs=s
        ans = i
print ans+1
