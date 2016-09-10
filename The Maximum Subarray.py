# Enter your code here. Read input from STDIN. Print output to STDIN
def splitMax(a,b):
    maxa = -999999999
    maxb = -999999999
    suma = 0
    sumb = 0
    for i in range(len(a)-1,-1,-1):
        suma+=a[i]
        if suma>maxa:
            maxa=suma
    for i in range(len(b)):
        sumb+=b[i]
        if sumb>maxb:
            maxb=sumb
    #print a,b,maxa,maxb
    return maxa+maxb

def countMax(a):
    if len(a)==1:
        return a[0]
    else:
        l = len(a)
        return max(countMax(a[:l/2]),countMax(a[l/2:]),splitMax(a[:l/2],a[l/2:]))

def nonContSum(arr):
    temp = filter(lambda x:x>=0,arr)
    if len(temp)==0:
        return max(arr)
    return sum(temp)
        
for i in xrange(input()):
    n = input()
    arr = map(int,raw_input().split())
    print countMax(arr),nonContSum(arr)
    
    