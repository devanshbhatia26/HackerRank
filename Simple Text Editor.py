s = ""
stack = []
for i in range(input()):
    query = raw_input().strip().split()
    query[0] = int(query[0])
    if query[0]==1:
        s+=query[1]
        stack.append((1,len(query[1])))
    elif query[0]==2:
        query[1]=int(query[1])
        stack.append((0,s[len(s)-query[1]:]))
        s=s[:len(s)-query[1]]
    elif query[0]==3:
        print s[int(query[1])-1]
    elif query[0]==4:
        if stack:
            temp = stack.pop()
            if temp[0]==1:
                s=s[:-temp[1]]
            elif temp[0]==0:
                s+=temp[1]
