# o/p
# 14
# 14 

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        if self.second:
            return self.second[-1]
        return self.first[0]
    
    def pop(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        self.second.pop()
    
    def put(self, value):
        self.first.append(value)

queue = MyQueue()
fin = open('two_stacks_inp.txt', 'r')
# t = int(raw_input())
t = int(fin.readline().strip())
for line in xrange(t):
    values = map(int, fin.readline().strip().split())
    # values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()