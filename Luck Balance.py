# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = map(int,raw_input().split())
contests = []
for i in range(n):
    contests.append(map(int,raw_input().split()))
imp = sorted((i[0] for i in filter(lambda x:x[1]==1,contests)), key=lambda y:y,reverse=True)
unimp = [i[0] for i in filter(lambda x:x[1]==0,contests)]
#print imp
#print unimp
luck = sum(imp[:k])
print luck+sum(unimp)-sum(imp[k:])