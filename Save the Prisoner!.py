for _ in range(input()):
    n,m,s = map(int,raw_input().split())
    actual = m%n
    if actual+s>n:
        ans = (actual+s)-n-1
    else:
        ans = actual+s-1
    if ans==0:
        print n
    else:
        print ans