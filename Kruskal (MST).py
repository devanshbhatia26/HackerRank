n,m = map(int,raw_input().strip().split())
dist = {}
for i in range(m):
    a,b,c = map(int,raw_input().strip().split())
    if (a-1,b-1) in dist.keys() and dist[(a-1,b-1)]<=c:
        continue
    dist[(a-1,b-1)]=c
    dist[(b-1,a-1)]=c
ans = 0
conn = range(n)
def union(u,v):
	global conn
	global n
	if conn[u]!=conn[v]:
		mi = min(conn[u],conn[v])
		ma = max(conn[u],conn[v])
		for i in range(n):
			if conn[i]==ma:
				conn[i]=mi

def find(u,v):
	return conn[u]==conn[v]

order = sorted(dist.keys(),key = lambda x : dist[x])

for edge in order:
	if conn.count(min(conn))==n:
		break
	if find(edge[0],edge[1]):
		continue
	else:
		union(edge[0],edge[1])
		ans+=dist[edge]
		
print ans