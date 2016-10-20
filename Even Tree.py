class node:
   
    def __init__(self,num):
        self.num = num
        self.parent = None
        self.child = []
    
    def setParent(self,p):
        self.parent = p
    
    def addChild(self,c):
        self.child.append(c)
    
    def children(self):
        return self.child
    
n,m = map(int,raw_input().strip().split())

nodes = [node(i) for i in range(1,n+1)]
nodes.insert(0,None)

for i in range(m):
    a,b = map(int,raw_input().strip().split())
    nodes[a].setParent(nodes[b])
    nodes[b].addChild(nodes[a])

def noOfChildren(i):
    ptr = 0 
    queue = [nodes[i]]
    while ptr!=len(queue):
        queue = queue + queue[ptr].children()
        ptr+=1
    return ptr

print len(filter(lambda x:x%2==0,map(noOfChildren,range(1,n+1))))-1
