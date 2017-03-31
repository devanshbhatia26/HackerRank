n = input()
arr = map(int,raw_input().strip().split())
ans = 0
for i in range(n):
    temp = i
    count = 1
    temp1 = 0
    while temp>=0 and arr[temp]>=arr[i]:
        temp1 = max(temp1,count*arr[i])
        temp-=1
        count+=1
    temp = i
    count = 1
    temp2 = 0
    while temp<n and arr[temp]>=arr[i]:
        temp2 = max(temp2,count*arr[i])
        count+=1
        temp+=1
    ans = max(ans,temp1+temp2-arr[i])
print ans
