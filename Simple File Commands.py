import sys
from collections import *
from heapq import *

have = defaultdict(int)

d = Counter()

d2 = defaultdict(list)
 
q = int(raw_input().strip())

def separate(s):
    ind = s.rfind('(')
    if ind==-1:
        return s,0
    return s[:ind],int(s[ind+1:len(s)-1])

lastval = defaultdict(list)

def ins(command):
    s,dg = separate(command[1])    
    if d[s]>0:
        heapify(lastval[s])
        place = heappop(lastval[s])
        if place>=d[s]:
            d[s] += 1
            d2[s].append(1)
            place = d[s]-1
            lastval[s].append(d[s])
        else:
            d2[s][place] = 1
        
        if place>0:
            s += '('+str(place)+')'
        have[s] = 1
        return s
    else:
        d[s] = 1
        d2[s].append(1)
        have[s] = 1
        lastval[s].append(1)
        return s

def dele(command):
    s,d = separate(command[1])
    have[command[1]]=0
    d2[s][d] =0
    lastval[s].append(d)
    return command[1]

for a0 in xrange(q):
    command = raw_input().strip().split()
    if command[0]=='crt':
        s = ins(command)
        print '+',s
    elif command[0]=='del':
        s = dele(command)
        print '-',s
    elif command[0]=='rnm':
        s2 = dele(['del',command[1]])
        s1 = ins(['crt',command[2]])
        print 'r',s2,'->',s1
