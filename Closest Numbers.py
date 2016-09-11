n = input()
arr = sorted(map(int,raw_input().strip().split()))
ans = []
mini = 999999999
for i in range(len(arr)-1):
    if abs(arr[i]-arr[i+1])<mini:
        mini = abs(arr[i]-arr[i+1])
        ans = [(arr[i],arr[i+1])]
    elif abs(arr[i]-arr[i+1])==mini:
        ans.append((arr[i],arr[i+1]))

print " ".join([" ".join(map(str,x)) for x in ans])