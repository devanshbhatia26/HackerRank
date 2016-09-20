for i in range(input()):
    n,m = map(int,raw_input().strip().split())
    adj = [[] for i in range(n)]

    for i in range(m):
        a,b = map(int,raw_input().strip().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    src = input()
    src-=1

    dist = [-1]*(n)

    queue = [src]
    ptr = 0
    dist[src]=0
    while ptr<len(queue):
        for v in adj[queue[ptr]]:
            if dist[v]==-1:
                queue.append(v)
                dist[v]=dist[queue[ptr]]+1
        ptr+=1

    for i in range(n):
        if dist[i]!=-1:
            dist[i]*=6
    print " ".join(map(str,filter(lambda x:x!=0,dist)))
