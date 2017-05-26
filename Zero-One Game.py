class stack:
    
    def __init__(self):
        self.top = -1
        self.st = []
    
    def push(self,n):
        self.st.append(n)
        self.top+=1
    
    def pop(self):
        if self.top==-1:
            return
        self.top-=1
        return self.st.pop()
    
    def peek(self):
        return self.st[self.top]
    
    def isEmpty(self):
        if self.top==-1:
            return True
        return False

    def size(self):
        return self.top+1

    def values(self):
        return self.st[:]
import sys
import re

pattern = re.compile(r'0.0')

g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    sequence = map(int, raw_input().strip().split(' '))
    # If Alice wins, print 'Alice' on a new line; otherwise, print 'Bob'
    count = 0
    l = len(sequence)
    st = stack()
    st.push(sequence[0])
    for i in range(1,l-1):
        if st.peek()==0 and sequence[i+1]==0:
            count+=1
            temp = st.pop()
            if not st.isEmpty():
                while not st.isEmpty() and sequence[i+1]==0 and st.peek()==0:
                    count+=1
                    temp = st.pop()
            st.push(temp)
        else:
            st.push(sequence[i])
                
        #print st.values()
    #print count
    if count%2:
        print "Alice"
    else:
        print "Bob"
