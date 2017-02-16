primes = [0,2,3,5,7,11,13,17,19,23,29]

def check(a,l):
    for x in l[1:]:
        if a%x==0:
            return False
    return True
def prime(n):
    if len(primes)>n:
        return primes[n]
    else:
        while len(primes)<=n:
            temp = primes[-1]+1
            while not check(temp,primes):
                temp+=1
            primes.append(temp)
    return primes[n]

n,q = map(int,raw_input().strip().split())
a = map(int,raw_input().strip().split())
ans = []
for i in range(1,q+1):
    temp = []
    temp2 = []
    p = prime(i)
    for j in range(len(a)-1,-1,-1):
        if a[j]%p==0:
            temp2.append(a[j])
        else:
            temp.append(a[j])
    ans.extend(reversed(temp2))
    a = temp[:]
    if len(a)==0:
        break
    #print ans,temp
a.reverse()
print "\n".join(map(str,ans+a))

