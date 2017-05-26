def getMaxMonsters(n, hit, t, h):
    h = sorted(h)
    ans = 0
    for i in range(n):
        if h[i]<=(t*hit):
            temp = h[i]/hit + int(h[i]%hit!=0)
            t -= temp
            if t>=0:
                ans +=1
        #print t,ans,h
        if t<=0:
            break
    return ans
        
    
    
n, hit, t = raw_input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = map(int, raw_input().strip().split(' '))
result = getMaxMonsters(n, hit, t, h)
print(result)

