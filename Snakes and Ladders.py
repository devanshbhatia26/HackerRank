from collections import defaultdict

def BFS(graph,ladders,snakes):
    src = 1
    dest = 100
    queue = [src]
    ptr = 0
    prev = [None]*101
    while dest not in queue:
        temp = 0
        for v in graph[queue[ptr]]:
            if v not in queue:
                queue.append(v)
                prev[v] = queue[ptr]
        ptr+=1
        if ptr >= len(queue):
            return -1
    #print queue
    #print prev
    x = 100
    steps = 0
    #print queue
    #print prev
    #print ladders
    #print snakes
    while prev[x]!=None:
        if prev[x] not in ladders and prev[x] not in snakes:
            steps+=1
        x = prev[x]
    return steps

for _ in range(input()):
    
    graph = defaultdict(list)
    ladders = []
    snakes = []
    
    noOfLadders = input()
    for l in range(noOfLadders):
        a,b = map(int,raw_input().strip().split())
        graph[a].append(b)
        ladders.append(a)
    noOfSnakes = input()
    for s in range(noOfSnakes):
        a,b = map(int,raw_input().strip().split())
        graph[a].append(b)
        snakes.append(a)
    
    for i in range(1,100):
        if i not in ladders and i not in snakes:
            graph[i].append(i+1)
    
    for i in range(1,99):
        if i not in ladders and i not in snakes:
            graph[i].append(i+2)
    
    for i in range(1,98):
        if i not in ladders and i not in snakes:
            graph[i].append(i+3)
    
    for i in range(1,97):
        if i not in ladders and i not in snakes:
            graph[i].append(i+4)
    
    for i in range(1,96):
        if i not in ladders and i not in snakes:
            graph[i].append(i+5)
    
    for i in range(1,95):
        if i not in ladders and i not in snakes:
            graph[i].append(i+6)
    
    
    print BFS(graph,ladders,snakes)
    