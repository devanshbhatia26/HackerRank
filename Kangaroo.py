import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if v2!=v1 and (x1-x2)%(v2-v1)==0 and (x1-x2)/(v2-v1)>=0:
    print "YES"
else:
    print "NO"