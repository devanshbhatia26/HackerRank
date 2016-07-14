a,b,c = map(int,raw_input().split())
stackA = map(int,raw_input().split())
sA = sum(stackA)
stackB = map(int,raw_input().split())
sB = sum(stackB)
stackC = map(int,raw_input().split())
sC = sum(stackC)
while True:
    if sA==sB and sB==sC:
        print sA
        break
    else:
        if sA>=sB and sA>=sC:
            sA-=stackA[0]
            del stackA[0]
        elif sB>=sA and sB>=sC:
            sB-=stackB[0]
            del stackB[0]
            
        elif sC>=sA and sC>=sB:
            sC-=stackC[0]
            del stackC[0]
    