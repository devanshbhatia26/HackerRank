from collections import Counter
n = 0
l = input()
a = map(int,raw_input().split())
b = map(int,raw_input().split())
countA = Counter(a)
countB = Counter(b)
for char in countA.keys():
    minim = min(countA[char],countB[char])
    if minim == countA[char]:
        countB[char] -= countA[char]
        n += countA[char]
        countA[char] = 0
    else:
        countA[char] -= countB[char]
        n += countB[char]
        countB[char] = 0
if countA.values().count(1)==0 or countB.values().count(1)==0:
    print n-1
elif countB.values().count(1)==0:
    print n
else:
    print n+1